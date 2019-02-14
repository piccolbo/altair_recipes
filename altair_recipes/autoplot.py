"""Automatic plot selection."""
from .barchart import barchart
from .boxplot import boxplot
from .common import col_cardinality
from .heatmap import heatmap
from .histogram import histogram
from .scatterplot import scatterplot
from .signatures import multivariate_recipe
from .stripplot import stripplot
from autosig import autosig
from numbers import Number
import pandas as pd


def bin_midpoints(xx, n):
    """Divide a vector in equal-width bins and return the midpoints if it is Numeric, otherwise the vector itself.

    Parameters
    ----------
    xx : Iterable
        The vector to be binned or other iterable to return as-is.
    n : integer
        Number of bins.

    Returns
    -------
    list or same as xx
        The midpoints or xx itself.

    """
    return (
        list(map(lambda x: x.mid, list(pd.cut(xx, n))))
        if issubclass(type(xx.iloc[0]), Number)
        else xx
    )


def overlap(data):
    """Find how dense a set of points is in relation to plotting them.

    Parameters
    ----------
    data : DataFrame
        The data whose density needs to be evaluated.

    Returns
    -------
    integer
        The maximum number of data points having identical coordinates on categorical dimensions or falling within the same bin when Numeric, after an equal-width binning operation into 100 bins (100 is somewhat arbitrary, experience based).

    """
    return data.apply(bin_midpoints, n=100).groupby(list(data.columns)).size().max()


def is_cat(xx):
    """Whether a list or vector is categorical (non Numeric).

    Parameters
    ----------
    xx : list or vector
        A list or vector.

    Returns
    -------
    bool
        Whether `xx` is categorical.

    """
    return not issubclass(type(xx.iloc[0]), Number)


@autosig(multivariate_recipe)
def autoplot(data, columns=None, group_by=None, height=600, width=800):
    """Automatically choose and produce a statistical graphics based on up to three columns of data."""

    assert group_by is None, "long data not supported yet"
    vars_n = len(columns)
    assert vars_n <= 3, "Only up to three vars supported at this time"
    data = data[columns]
    columns = sorted(columns, key=lambda x: -len(data[x].unique()))
    y, x, z, *_ = columns + 2 * [None]
    overlap_deg = overlap(data[columns[: min(vars_n, 2)]])
    max_overlap = 10
    high_overlap = overlap_deg >= max_overlap
    no_overlap = overlap_deg == 1
    low_overlap = 1 < overlap_deg < max_overlap
    cat_vars_n = sum(map(lambda col: is_cat(data[col]), columns))
    numeric_vars_n = vars_n - cat_vars_n

    chart_type_selection = [
        (scatterplot, numeric_vars_n >= 2 and not high_overlap),
        (heatmap, numeric_vars_n >= 2 and high_overlap),
        (stripplot, numeric_vars_n == 1 and not high_overlap),
        (barchart, numeric_vars_n == 0),
        (histogram, numeric_vars_n == 1 and cat_vars_n == 0 and high_overlap),
        (boxplot, numeric_vars_n == 1 and cat_vars_n >= 1 and high_overlap),
    ]
    chart_type = list(filter(lambda x: x[1], chart_type_selection))
    assert len(chart_type) == 1
    chart_type = chart_type[0][0]
    use_facet = cat_vars_n >= 2 or (
        cat_vars_n == 1 and numeric_vars_n == 2 and not no_overlap
    )
    use_color = vars_n == 3 and not (use_facet and chart_type is scatterplot)
    use_opacity = (chart_type in (scatterplot, stripplot) and low_overlap) or (
        chart_type is heatmap and high_overlap and numeric_vars_n == 3
    )  # heat

    if chart_type is barchart:
        args = dict(x=y, y="count()", height=height, width=width)
        if use_facet:
            args.update(x=x, color=x, width=width // col_cardinality(data, y))
            facet_args = dict(column=y)
            if z is not None:
                args.update(height=height // col_cardinality(data, z))
                facet_args.update(row=z)
        chart = barchart(data, **args)
        if use_facet:
            chart = chart.facet(**facet_args)

    if chart_type is boxplot:
        chart = boxplot(
            data,
            columns=y,
            group_by=x,
            color=use_facet,  # this is a redundant use of color, different from necessary uses. Encodes x again
            height=height,
            width=width // col_cardinality(data, z),
        )
        if use_facet:
            chart = chart.facet(column=z)
    if chart_type is heatmap:
        args = dict(color="count()")
        if use_opacity:
            args.update(color=z, opacity="count()")
        chart = heatmap(
            data,
            x=x,
            y=y,
            aggregate="average" if use_opacity else "count",
            height=height // col_cardinality(data, z, use_facet),
            width=width // col_cardinality(data, z, use_facet),
            **args
        )
        if use_facet:
            chart = chart.facet(row=z)
    if chart_type is histogram:
        chart = histogram(data, column=y, height=height, width=width)
    if chart_type is stripplot:
        chart = stripplot(
            data,
            columns=y,
            group_by=x,
            color=x if use_facet else None,
            opacity=1 / overlap_deg if use_opacity else 1,
            height=height,
            width=width // col_cardinality(data, z, use_facet),
        )
        if use_facet:
            chart = chart.facet(column=z)
    if chart_type is scatterplot:
        chart = scatterplot(
            data,
            x=x,
            y=y,
            color=z if use_color else None,
            opacity=1 / overlap_deg if use_opacity else 1,
            height=height // col_cardinality(data, z, use_facet),
            width=width // col_cardinality(data, z, use_facet),
        )
        if use_facet:
            chart = chart.facet(row=z)
    return chart
