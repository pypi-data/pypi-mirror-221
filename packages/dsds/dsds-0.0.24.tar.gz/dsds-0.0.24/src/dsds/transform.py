from __future__ import annotations

from .type_alias import (
    PolarsFrame
    , ImputationStrategy
    , ScalingStrategy
    , PowerTransformStrategy
    , DateExtract
    , ListExtract
    , HorizontalExtract
    , ZeroOneCombineRules
    , clean_strategy_str
)
from .prescreen import type_checker
from .blueprint import( # Need this for Polars extension to work
    Blueprint  # noqa: F401
)
from typing import Optional, Union
from scipy.stats import (
    yeojohnson_normmax
    , boxcox_normmax
)
import logging
import math
# import numpy as np
import polars as pl

# A lot of companies are still using Python < 3.10
# So I am not using match statements

logger = logging.getLogger(__name__)

def impute(
    df:PolarsFrame
    , cols:list[str]
    , strategy:ImputationStrategy = 'median'
    , const:float = 1.
) -> PolarsFrame:
    '''
    Impute the given columns with the given strategy.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars DataFrame
    cols
        The columns to impute
    strategy
        One of 'median', 'mean', 'const' or 'mode'. If 'const', the const argument should be provided. Note that
        if strategy is mode and if two values occur the same number of times, a random one will be picked.
    const
        The constant value to impute by if strategy = 'const'    
    '''
    s = clean_strategy_str(strategy)
    if s == "median":
        all_medians = df.lazy().select(cols).median().collect().row(0)
        exprs = (pl.col(c).fill_null(all_medians[i]) for i,c in enumerate(cols))
    elif s in ("mean", "avg", "average"):
        all_means = df.lazy().select(cols).mean().collect().row(0)
        exprs = (pl.col(c).fill_null(all_means[i]) for i,c in enumerate(cols))
    elif s in ("const", "constant"):
        exprs = (pl.col(c).fill_null(const) for c in cols)
    elif s in ("mode", "most_frequent"):
        all_modes = df.lazy().select(cols).select(pl.all().mode().first()).collect().row(0)
        exprs = (pl.col(c).fill_null(all_modes[i]) for i,c in enumerate(cols))
    else:
        raise TypeError(f"Unknown imputation strategy: {strategy}")

    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(list(exprs))
    return df.with_columns(exprs)

def scale(
    df:PolarsFrame
    , cols:list[str]
    , strategy:ScalingStrategy="standard"
    , const:float = 1.0
) -> PolarsFrame:
    '''
    Scale the given columns with the given strategy.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars DataFrame
    cols
        The columns to scale
    strategy
        One of 'standard', 'min_max', 'const'. If 'const', the const argument should be provided
    const
        The constant value to scale by if strategy = 'const'    
    '''
    _ = type_checker(df, cols, "numeric", "scale")
    s = clean_strategy_str(strategy)
    if s == "standard":
        mean_std = df.lazy().select(cols).select(
            pl.all().mean().prefix("mean:")
            , pl.all().std().prefix("std:")
        ).collect().row(0)
        exprs = ( (pl.col(c) - mean_std[i])/(mean_std[i + len(cols)]) for i,c in enumerate(cols) )
    elif s == "min_max":
        min_max = df.lazy().select(cols).select(
            pl.all().min().prefix("min:"),
            pl.all().max().prefix("max:")
        ).collect().row(0) # All mins come first, then maxs
        exprs = ( (pl.col(c) - min_max[i])/((min_max[i + len(cols)] - min_max[i])) for i,c in enumerate(cols) )
    elif s in ("const", "constant"):
        exprs = (pl.col(c)/const for c in cols)
    else:
        raise TypeError(f"Unknown scaling strategy: {strategy}")

    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(list(exprs))
    return df.with_columns(exprs)

def merge_infreq_values(
    df: PolarsFrame
    , cols: list[str]
    , min_count: Optional[int] = 10
    , min_frac: Optional[float] = None
    , separator: str = '|'
) -> PolarsFrame:
    '''
    Combines infrequent categories in string columns together.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars DataFrame
    cols
        List of string columns to perform this operation
    min_count
        Define a category to be infrequent if it occurs less than min_count. This defaults to 10 if both min_count and 
        min_frac are None.
    min_frac
        Define category to be infrequent if it occurs less than this percentage of times. If both min_count and min_frac
        are set, min_frac takes priority
    separator
        The separator for the new value representing the combined categories

    Example
    -------
    >>> import dsds.transform as t
    ... df = pl.DataFrame({
    ...     "a":["a", "b", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c", "c"],
    ...     "b":["a", "b", "c", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d", "d"]
    ... })
    >>> df
    shape: (14, 2)
    ┌─────┬─────┐
    │ a   ┆ b   │
    │ --- ┆ --- │
    │ str ┆ str │
    ╞═════╪═════╡
    │ a   ┆ a   │
    │ b   ┆ b   │
    │ c   ┆ c   │
    │ c   ┆ d   │
    │ …   ┆ …   │
    │ c   ┆ d   │
    │ c   ┆ d   │
    │ c   ┆ d   │
    │ c   ┆ d   │
    └─────┴─────┘
    >>> t.merge_infreq_values(df, ["a", "b"], min_count=3)
    shape: (14, 2)
    ┌─────┬───────┐
    │ a   ┆ b     │
    │ --- ┆ ---   │
    │ str ┆ str   │
    ╞═════╪═══════╡
    │ a|b ┆ a|c|b │
    │ a|b ┆ a|c|b │
    │ c   ┆ a|c|b │
    │ c   ┆ d     │
    │ …   ┆ …     │
    │ c   ┆ d     │
    │ c   ┆ d     │
    │ c   ┆ d     │
    │ c   ┆ d     │
    └─────┴───────┘
    '''
    _ = type_checker(df, cols, "string", "merge_infreq_values")
    if min_frac is None:
        if min_count is None:
            comp = pl.col("count") < 10
        else:
            comp = pl.col("count") < min_count
    else:
        comp = pl.col("count")/pl.col("count").sum() < min_frac

    exprs = []
    for c in cols:
        infreq = df.lazy().groupby(c).count().filter(
            comp
        ).collect().get_column(c)
        value = separator.join(infreq)
        exprs.append(
            pl.when(pl.col(c).is_in(infreq)).then(value).otherwise(pl.col(c)).alias(c)
        )
    
    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(exprs)
    return df.with_columns(exprs)

def combine_zero_ones(
    df: PolarsFrame
    , cols: list[str]
    , new_name: str
    , rule: ZeroOneCombineRules = "union"
    , drop_original:bool = True
) -> PolarsFrame:
    '''
    Take columns that are all binary 0, 1 columns, combine them according to the rule. Please make sure 
    the columns only contain binary 0s and 1s. Depending on the rule, this can be used, for example, to 
    quickly combine many one hot encoded columns into one, or reducing the same binary columns into one.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars DataFrame
    cols
        List of binary 0, 1 columns to combine
    new_name
        Name for the combined column
    rule
        One of 'union', 'intersection', 'same'.
    drop_original
        If true, drop column in cols

    Examples
    --------
    >>> import dsds.transform as t
    ... df = pl.DataFrame({
    ...     "a": [1, 1, 0],
    ...     "b":[1, 0, 1],
    ...     "c":[1, 1, 1]
    ... })
    >>> t.combine_zero_ones(df, cols=["a", "b", "c"], new_name="abc", rule="same")
    shape: (3, 1)
    ┌─────┐
    │ abc │
    │ --- │
    │ u8  │
    ╞═════╡
    │ 1   │
    │ 0   │
    │ 0   │
    └─────┘
    >>> t.combine_zero_ones(df, cols=["a", "b", "c"], new_name="abc", rule="union")
    shape: (3, 1)
    ┌─────┐
    │ abc │
    │ --- │
    │ u8  │
    ╞═════╡
    │ 1   │
    │ 1   │
    │ 1   │
    └─────┘
    '''
    if rule == "union":
        expr = pl.max_horizontal([pl.col(c) for c in cols]).cast(pl.UInt8).alias(new_name)
    elif rule == "intersection":
        expr = pl.min_horizontal([pl.col(c) for c in cols]).cast(pl.UInt8).alias(new_name)
    elif rule == "same":
        expr = pl.when(sum(pl.col(c) for c in cols).is_in((0, len(cols)))).then(
                    pl.lit(1, dtype=pl.UInt8)
                ).otherwise(
                    pl.lit(0, dtype=pl.UInt8)
                ).alias(new_name)
    else:
        raise TypeError(f"The input `{rule}` is not a valid ZeroOneCombineRule.")

    if isinstance(df, pl.LazyFrame):
        if drop_original:
            return df.blueprint.with_columns(expr).blueprint.drop(cols)
        return df.blueprint.with_columns(expr)
    if drop_original:
        return df.with_columns(expr).drop(cols)
    return df.with_columns(expr)

def power_transform(
    df: PolarsFrame
    , cols: list[str]
    , strategy: PowerTransformStrategy = "yeo_johnson"
    # , lmbda: Optional[float] = None
) -> PolarsFrame:
    '''
    Performs power transform on the numerical columns.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and must all be numerical
    strategy
        Either 'yeo_johnson' or 'box_cox'
    '''
    _ = type_checker(df, cols, "numeric", "power_transform")
    s = clean_strategy_str(strategy)
    exprs:list[pl.Expr] = []
    # Ensure columns do not have missing values
    non_null_list = []
    with_null_list = []
    for c, count in zip(cols, df.lazy().select(cols).null_count().collect().row(0)):
        if count > 0:
            with_null_list.append(c)
        else:
            non_null_list.append(c)

    if len(with_null_list) > 0:
        logger.info("The following columns will not be processed by power_transform because they contain missing "
                    f"values. Please impute them:\n{with_null_list}")
        
    if s in ("yeo_johnson", "yeojohnson"):
        lmaxs = df.lazy().select(non_null_list).groupby(1).agg(
            pl.all()
            .apply(lambda x: yeojohnson_normmax(x))
            .cast(pl.Float64)
        ).select(non_null_list).collect().row(0)
        for c, lmax in zip(non_null_list, lmaxs):
            if lmax == 0: # log(x + 1)
                x_ge_0_sub_expr = (pl.col(c).add(1)).log()
            else: # ((x + 1)**lmbda - 1) / lmbda
                x_ge_0_sub_expr = ((pl.col(c).add(1)).pow(lmax) - 1) / lmax

            if lmax == 2: # -log(-x + 1)
                x_lt_0_sub_expr = pl.lit(-1) * (1 - pl.col(c)).log()
            else: #  -((-x + 1)**(2 - lmbda) - 1) / (2 - lmbda)
                t = 2 - lmax
                x_lt_0_sub_expr = pl.lit(-1/t) * ((1 - pl.col(c)).pow(t) - 1)

            exprs.append(
                pl.when(pl.col(c).ge(0)).then(x_ge_0_sub_expr).otherwise(x_lt_0_sub_expr).alias(c)
            )
    elif s in ("box_cox", "boxcox"):
        lmaxs = df.lazy().select(non_null_list).groupby(1).agg(
            pl.all()
            .apply(lambda x: boxcox_normmax(x, method="mle"))
            .cast(pl.Float64)
        ).select(non_null_list).collect().row(0)
        exprs.extend(
            pl.col(c).log() if lmax == 0 else (pl.col(c).pow(lmax) - 1) / lmax 
            for c, lmax in zip(non_null_list, lmaxs)
        )
    else:
        raise TypeError(f"The input strategy {strategy} is not a valid strategy. Valid strategies are: yeo_johnson "
                        "or box_cox")
    
    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(exprs)
    return df.with_columns(exprs)

def normalize(
    df: PolarsFrame
    , cols:list[str]
) -> PolarsFrame:
    '''
    Normalize the given columns by dividing them with the respective column sum.

    !!! Note this will NOT be remembered by the blueprint !!!

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and should all be numeric columns
    '''
    _ = type_checker(df, cols, "numeric", "normalize")
    return df.with_columns(pl.col(c)/pl.col(c).sum() for c in cols)

def clip(
    df: PolarsFrame
    , cols: list[str]
    , min_clip: Optional[float] = None
    , max_clip: Optional[float] = None
) -> PolarsFrame:
    '''
    Clips the columns within the min and max_clip bounds. This can be used to control outliers. If both min_clip and
    max_clip are provided, perform two-sided clipping. If only one bound is provided, only one side will be clipped.
    It will throw an error if both min and max_clips are not provided.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and should all be numeric columns
    min_clip
        Every value smaller than min_clip will be replaced by min_cap
    max_clip
        Every value bigger than max_clip will be replaced by max_cap
    '''
    _ = type_checker(df, cols, "numeric", "clip")
    a:bool = min_clip is None
    b:bool = max_clip is None
    if a & (not b):
        exprs = (pl.col(c).clip_max(max_clip) for c in cols)
    elif (not a) & b:
        exprs = (pl.col(c).clip_min(min_clip) for c in cols)
    elif not (a | b):
        exprs = (pl.col(c).clip(min_clip, max_clip) for c in cols)
    else:
        raise ValueError("At least one of min_cap and max_cap should be provided.")
    
    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(list(exprs))
    return df.with_columns(exprs)

def log_transform(
    df: PolarsFrame
    , cols:list[str]
    , base:float = math.e
    , cast_non_positive: Optional[float] = None
    , plus_one:bool = False
    , suffix:str = "_log"
) -> PolarsFrame:
    '''
    Performs classical log transform on the given columns, e.g. log(x). You may set plus_one to perform ln(1 + x).
    If you want to replace the original column, simply set suffix = "". If you intend to drop original columns, please
    insert a `dsds.prescreen.drop` step in the pipeline.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and should all be numeric columns
    base
        Base of log. Default is math.e
    cast_non_positive
        How to deal with non positive values (<=0). None means turn them into null
    plus_one
        If plus_one is true, this will perform ln(1+x) and ignore base and cast_non_positive arguments
    suffix
        Choice of a suffix to the transformed columns. If this is the empty string "", then the original column
        will be replaced. If plus_one = True, then suffix will always be "_log1p".
    '''
    _ = type_checker(df, cols, "numeric", "log_transform")
    if plus_one:
        exprs = (
            pl.col(c).log1p().suffix("_log1p") for c in cols
        )
    else:
        exprs = (
            pl.when(pl.col(c) <= 0).then(cast_non_positive).otherwise(pl.col(c).log(base)).suffix(suffix) for c in cols
        )
    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(list(exprs))
    return df.with_columns(exprs)

def extract_dt_features(
    df: PolarsFrame
    , cols: list[str]
    , extract: Union[DateExtract, list[DateExtract]] = ["year", "quarter", "month"]
    , sunday_first: bool = False
    , drop_original: bool = True
) -> PolarsFrame:
    '''
    Extracts additional date related features from existing date/datetime columns.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and should all be date/datetime columns
    extract
        One of "year", "quarter", "month", "week", "day_of_week", "day_of_year", or a list of these values 
        such as ["year", "quarter"], which means extract year and quarter from all the columns provided 
    sunday_first
        For day_of_week, by default, Monday maps to 1, and so on. If sunday_first = True, then Sunday will be
        mapped to 1 and so on
    drop_original
        Whether to drop columns in cols

    Example
    -------
    >>> import dsds.transform as t
    ... df = pl.DataFrame({
    ...     "date1":["2021-01-01", "2022-02-03", "2023-11-23"]
    ...     , "date2":["2021-01-01", "2022-02-03", "2023-11-23"]
    ... }).with_columns(
    ...     pl.col(c).str.to_date() for c in ["date1", "date2"]
    ... )
    >>> print(df)
    shape: (3, 2)
    ┌────────────┬────────────┐
    │ date1      ┆ date2      │
    │ ---        ┆ ---        │
    │ date       ┆ date       │
    ╞════════════╪════════════╡
    │ 2021-01-01 ┆ 2021-01-01 │
    │ 2022-02-03 ┆ 2022-02-03 │
    │ 2023-11-23 ┆ 2023-11-23 │
    └────────────┴────────────┘
    >>> cols = ["date1", "date2"]
    >>> print(t.extract_dt_features(df, cols=cols, drop_original=False))
    shape: (3, 8)
    ┌────────────┬────────────┬────────────┬───────────┬───────────┬───────────┬───────────┬───────────┐
    │ date1      ┆ date2      ┆ date1_year ┆ date2_yea ┆ date1_qua ┆ date2_qua ┆ date1_mon ┆ date2_mon │
    │ ---        ┆ ---        ┆ ---        ┆ r         ┆ rter      ┆ rter      ┆ th        ┆ th        │
    │ date       ┆ date       ┆ u32        ┆ ---       ┆ ---       ┆ ---       ┆ ---       ┆ ---       │
    │            ┆            ┆            ┆ u32       ┆ u32       ┆ u32       ┆ u32       ┆ u32       │
    ╞════════════╪════════════╪════════════╪═══════════╪═══════════╪═══════════╪═══════════╪═══════════╡
    │ 2021-01-01 ┆ 2021-01-01 ┆ 2021       ┆ 2021      ┆ 1         ┆ 1         ┆ 1         ┆ 1         │
    │ 2022-02-03 ┆ 2022-02-03 ┆ 2022       ┆ 2022      ┆ 1         ┆ 1         ┆ 2         ┆ 2         │
    │ 2023-11-23 ┆ 2023-11-23 ┆ 2023       ┆ 2023      ┆ 4         ┆ 4         ┆ 11        ┆ 11        │
    └────────────┴────────────┴────────────┴───────────┴───────────┴───────────┴───────────┴───────────┘
    '''
    _ = type_checker(df, cols, "datetime", "extract_dt_features")
    exprs = []
    if isinstance(extract, list):
        to_extract = extract
    else:
        to_extract = [extract]
    
    for e in to_extract:
        if e == "month":
            exprs.extend(pl.col(c).dt.month().suffix("_month") for c in cols)
        elif e == "year":
            exprs.extend(pl.col(c).dt.year().suffix("_year") for c in cols)
        elif e == "quarter":
            exprs.extend(pl.col(c).dt.quarter().suffix("_quarter") for c in cols)
        elif e == "week":
            exprs.extend(pl.col(c).dt.week().suffix("_week") for c in cols)
        elif e == "day_of_week":
            if sunday_first:
                exprs.extend(
                    pl.when(pl.col(c).dt.weekday() == 7).then(1).otherwise(pl.col(c).dt.weekday()+1)
                    .suffix("_day_of_week") 
                    for c in cols
                )
            else:
                exprs.extend(pl.col(c).dt.weekday().suffix("_day_of_week") for c in cols)
        elif e == "day_of_year":
            exprs.extend(pl.col(c).dt.ordinal_day().suffix("_day_of_year") for c in cols)
        else:
            logger.info(f"Found {e} in extract, but it is not a valid DateExtract value. Ignored.")

    if isinstance(df, pl.LazyFrame):
        if drop_original:
            return df.blueprint.with_columns(exprs).blueprint.drop(cols)
        return df.blueprint.with_columns(exprs)
    if drop_original:
        return df.with_columns(exprs).drop(cols)
    return df.with_columns(exprs)
    
def extract_horizontally(
    df:PolarsFrame
    , cols: list[str]
    , extract: Union[HorizontalExtract, list[HorizontalExtract]] = ["min", "max"]
    , drop_original: bool = True
) -> PolarsFrame:
    '''
    Extract features horizontally across a few columns.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        List of columns to extract feature from
    extract
        One of "min", "max", "sum", "any", "all". Note that "any" and "all" only make practical sense when 
        all of cols are boolean columns, but they work even when cols are numbers.
    drop_original
        Whether to drop columns in cols

    Example
    -------
    >>> import dsds.transform as t
    ... df = pl.DataFrame({
    ...     "a":[1, 2, 3],
    ...     "b":[1, 2, 3],
    ...     "c":[1, 2, 3]
    ... })
    >>> t.extract_horizontally(df, cols=["a", "b", "c"], extract=["min", "max", "sum"])
    shape: (3, 3)
    ┌────────────┬────────────┬────────────┐
    │ min(a,b,c) ┆ max(a,b,c) ┆ sum(a,b,c) │
    │ ---        ┆ ---        ┆ ---        │
    │ i64        ┆ i64        ┆ i64        │
    ╞════════════╪════════════╪════════════╡
    │ 1          ┆ 1          ┆ 3          │
    │ 2          ┆ 2          ┆ 6          │
    │ 3          ┆ 3          ┆ 9          │
    └────────────┴────────────┴────────────┘
    '''
    if isinstance(extract, list):
        to_extract = extract
    else:
        to_extract = [extract]
    
    exprs = []
    for e in to_extract:
        if e == "min":
            exprs.append(pl.min_horizontal([pl.col(c) for c in cols]).alias(f"{e}({','.join(cols)})"))
        elif e == "max":
            exprs.append(pl.max_horizontal([pl.col(c) for c in cols]).alias(f"{e}({','.join(cols)})"))
        elif e == "sum":
            exprs.append(pl.sum_horizontal([pl.col(c) for c in cols]).alias(f"{e}({','.join(cols)})"))
        elif e == "any":
            exprs.append(pl.any_horizontal([pl.col(c) for c in cols]).alias(f"{e}({','.join(cols)})"))
        elif e == "all":
            exprs.append(pl.all_horizontal([pl.col(c) for c in cols]).alias(f"{e}({','.join(cols)})"))
        else:
            logger.info(f"Found {e} in extract, but it is not a valid HorizontalExtract value. Ignored.")

    if isinstance(df, pl.LazyFrame):
        if drop_original:
            return df.blueprint.with_columns(exprs).blueprint.drop(cols)
        return df.blueprint.with_columns(exprs)
    if drop_original:
        return df.with_columns(exprs).drop(cols)
    return df.with_columns(exprs)

def extract_list_features(
    df: PolarsFrame
    , cols: list[str]
    , extract: Union[ListExtract, list[ListExtract]] = ["min", "max"]
    , drop_original: bool = True
) -> PolarsFrame:
    '''
    Extract data from columns that contains lists.

    This will be remembered by blueprint by default.

    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    cols
        Must be explicitly provided and should all be date/datetime columns
    extract
        One of "min", "max", "mean", "len", "first", "last" or a list of these values such as ["min", "max"], 
        which means extract min and max from all the columns provided. Notice if mean is provided, then the 
        column must be list of numbers.
    drop_original
        Whether to drop columns in cols

    Example
    -------
    >>> import dsds.transform as t
    ... df = pl.DataFrame({
    ...     "a":[["a"],["b"], ["c"]],
    ...     "b":[[1,2], [3,3], [4,5,6]]
    ... })
    >>> t.extract_list_features(df, ["a","b"], extract=["min", "max", "len"])
    shape: (3, 6)
    ┌───────┬───────┬───────┬───────┬───────┬───────┐
    │ a_min ┆ b_min ┆ a_max ┆ b_max ┆ a_len ┆ b_len │
    │ ---   ┆ ---   ┆ ---   ┆ ---   ┆ ---   ┆ ---   │
    │ str   ┆ i64   ┆ str   ┆ i64   ┆ u32   ┆ u32   │
    ╞═══════╪═══════╪═══════╪═══════╪═══════╪═══════╡
    │ a     ┆ 1     ┆ a     ┆ 2     ┆ 1     ┆ 2     │
    │ b     ┆ 3     ┆ b     ┆ 3     ┆ 1     ┆ 2     │
    │ c     ┆ 4     ┆ c     ┆ 6     ┆ 1     ┆ 3     │
    └───────┴───────┴───────┴───────┴───────┴───────┘
    '''
    _ = type_checker(df, cols, "list", "extract_list_features")
    exprs = []
    if isinstance(extract, list):
        to_extract = extract
    else:
        to_extract = [extract]
    
    for e in to_extract:
        if e == "min":
            exprs.extend(pl.col(c).list.min().suffix("_min") for c in cols)
        elif e == "max":
            exprs.extend(pl.col(c).list.max().suffix("_max") for c in cols)
        elif e in ("mean", "avg"):
            exprs.extend(pl.col(c).list.mean().suffix("_mean") for c in cols)
        elif e == "len":
            exprs.extend(pl.col(c).list.lengths().suffix("_len") for c in cols)
        elif e == "first":
            exprs.extend(pl.col(c).list.first().suffix("_first") for c in cols)
        elif e == "last":
            exprs.extend(pl.col(c).list.last().suffix("_last") for c in cols)
        else:
            logger.info(f"Found {e} in extract, but it is not a valid ListExtract value. Ignored.")

    if isinstance(df, pl.LazyFrame):
        if drop_original:
            return df.blueprint.with_columns(exprs).blueprint.drop(cols)
        return df.blueprint.with_columns(exprs)
    if drop_original:
        return df.with_columns(exprs).drop(cols)
    return df.with_columns(exprs)

def moving_avgs(
    df:PolarsFrame
    , c: str
    , window_sizes:list[int]
    , min_periods: Optional[int] = None,
) -> PolarsFrame:
    '''
    Computes moving averages for column c with given window_sizes. Please make sure the dataframe is sorted
    before this. For a pipeline compatible sort, see `dsds.prescreen.order_by`.

    This will be remembered by blueprint by default.
    
    Parameters
    ----------
    df
        Either a lazy or eager Polars dataframe
    c
        Name of the column to compute moving averages
    window_sizes
        A list of positive integers > 1, representing the different moving average periods for the column c.
        Everything <= 1 will be ignored
    min_periods
        The number of values in the window that should be non-null before computing a result. If None, 
        it will be set equal to window size.
    '''
    exprs = (pl.col(c).rolling_mean(i, min_periods=min_periods).suffix(f"_ma_{i}") 
             for i in window_sizes if i > 1)
    if isinstance(df, pl.LazyFrame):
        return df.blueprint.with_columns(list(exprs))
    return df.with_columns(exprs)