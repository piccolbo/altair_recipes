"""Automatic plot selection."""
from .barchart import barchart
from .boxplot import boxplot
from .common import ndistinct
from .heatmap import heatmap
from .histogram import histogram
from .scatter import scatter
from .signatures import multivariate_recipe
from .stripplot import stripplot
from autosig import autosig
from numbers import Number
import pandas as pd


def binmid(xx, n):
    return (
        list(map(lambda x: x.mid, list(pd.cut(xx, n))))
        if issubclass(type(xx[0]), Number)
        else xx
    )


def overlap(data):
    return data.apply(binmid, n=100).groupby(list(data.columns)).size().max()


def var_order(data):
    cards = data.apply(lambda x: x.nunique())
    ranks = (-cards).rank(method="first")
    return pd.Series(ranks.index.values, index=pd.Series(ranks) - 1)


def is_cat(xx):
    return not issubclass(type(xx[0]), Number)


def resolve_var(n, nvars, order, data):
    return (order[n], is_cat(data[order[n]])) if nvars > n else (None, False)


@autosig(multivariate_recipe)
def autoplot(data, columns=None, group_by=None, height=600, width=800):
    """Automatically choose and produce a statistical graphics based on up to three columns of data"""
    assert group_by is None, "long data not supported yet"
    nvars = len(columns)
    assert nvars <= 3, "Only up to three vars supported at this time"
    data = data[columns]
    order = var_order(data)
    overlap_deg = (
        overlap(data[[order[0]]]) if nvars == 1 else overlap(data[[order[0], order[1]]])
    )
    OL_no = overlap_deg == 1
    OL_low = overlap_deg > 1 and overlap_deg <= 10
    OL_high = overlap_deg > 10

    all_cat_var = all([is_cat(data[col]) for col in columns])
    y, is_cat_y = resolve_var(0, nvars, order, data)
    x, is_cat_x = resolve_var(1, nvars, order, data)
    z, is_cat_z = resolve_var(2, nvars, order, data)
    nvcat = is_cat_x + is_cat_y + is_cat_z
    nvfloat = nvars - nvcat
    chart = None
    if all_cat_var and not OL_no:
        assert chart is None
        args = dict(x=y, y="count()", vfacet=z)
        if nvars >= 2:
            args.update(x=x, hfacet=y)
        chart = barchart(data, height=height, width=width, **args)
    if all_cat_var and OL_no:
        assert chart is None
        if nvars >= 2:
            args = dict(color=z) if z is not None else dict()
            chart = scatter(data, x=x, y=y, height=height, width=width, **args)
        else:  # nvars == 1
            chart = stripplot(data, columns=x, height=height, width=width)
    if nvfloat == 1 and nvcat >= 1 and OL_high:
        assert chart is None
        chart = boxplot(
            data, columns=y, group_by=x, color=z, height=height, width=width
        )
    if nvfloat >= 2 and OL_high:
        assert chart is None
        use_opacity = z is not None and not is_cat_z
        use_facet = z is not None and is_cat_z
        args = dict(color="count()")
        if use_opacity:
            args.update(color=z, opacity="count()")
        chart = heatmap(
            data,
            x=x,
            y=y,
            aggregate="average" if use_opacity else "count",
            height=height / ndistinct(data, z, use_facet),
            width=width / ndistinct(data, z, use_facet),
            **args
        )
        chart = chart.facet(row=z) if use_facet else chart
    if nvars == 1 and nvfloat == 1 and OL_high:
        assert chart is None
        chart = histogram(data, column=y, height=height, width=width)

    if nvfloat >= 2 and not OL_high:
        assert chart is None
        use_facet = z is not None and is_cat_z and OL_low
        use_color = z is not None and not use_facet
        use_opacity = (OL_low and not is_cat_z) or use_facet
        chart = scatter(
            data,
            x=x,
            y=y,
            color=z if use_color else None,
            opacity=1 / overlap_deg if use_opacity else 1,
            height=height / ndistinct(data, z, use_facet),
            width=width / ndistinct(data, z, use_facet),
        )
        chart = chart.facet(row=z) if use_facet else chart
    if nvfloat == 1 and not OL_high:
        assert chart is None
        use_facet = z is not None and is_cat_z and OL_low
        use_color = z is not None and not use_facet
        use_opacity = (OL_low and not is_cat_z) or use_facet
        chart = stripplot(
            data,
            columns=y,
            group_by=x,
            color=z if use_color else None,
            opacity=1 / overlap_deg if use_opacity else 1,
            height=height,
            width=width / ndistinct(data, z, use_facet),
        )
        chart = chart.facet(column=z) if use_facet else chart
    assert chart, "This combination was not foreseen"
    return chart
