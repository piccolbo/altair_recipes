"""Scatter plots."""
from .common import default
from .signatures import (
    bivariate_recipe,
    multivariate_recipe,
    color,
    tooltip,
)
import altair as alt
from autosig import autosig, Signature
from toolz.dicttoolz import keyfilter, valfilter


def keyvalfilter(keypred, valpred, a_dict):
    return keyfilter(keypred, valfilter(valpred, a_dict))


@autosig(bivariate_recipe + Signature(
    color=color(default=None, position=3),
    tooltip=tooltip(default=None, position=4)))
def scatter(data, x=0, y=1, color=None, tooltip=None):
    """Generate a scatter plot."""
    kwargs = keyvalfilter(lambda x: x in ['color', 'tooltip'],
                          lambda x: x is not None, locals())
    return alt.Chart(data).mark_point().encode(x=x, y=y, **kwargs)


@autosig(multivariate_recipe + Signature(
    color=color(default=None, position=3),
    tooltip=tooltip(default=None, position=4)))
def multiscatter(data, columns=None, group_by=None, color=None, tooltip=None):
    """Generate many scatter plots.

    Based on several columns, pairwise."""
    kwargs = keyvalfilter(lambda x: x in ['color', 'tooltip'],
                          lambda x: x is not None, locals())
    assert group_by is None, "Long format not supported yet"
    return alt.Chart(data).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'), **kwargs).repeat(
            row=columns, column=columns)
