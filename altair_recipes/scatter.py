"""Scatter plots."""
from .signatures import bivariate_recipe, multivariate_recipe, color, tooltip
import altair as alt
from autosig import autosig, Signature
from toolz.dicttoolz import keyfilter, valfilter


@autosig(
    bivariate_recipe
    + Signature(
        color=color(default=None, position=3), tooltip=tooltip(default=None, position=4)
    )
)
def scatter(data, x=0, y=1, color=None, tooltip=None, height=300, width=400):
    """Generate a scatter plot."""
    kwargs = keyfilter(
        lambda x: x in ["color", "tooltip"],
        valfilter(lambda x: x is not None, locals()),
    )
    return (
        alt.Chart(data, height=height, width=width)
        .mark_point()
        .encode(x=x, y=y, **kwargs)
    )


@autosig(
    multivariate_recipe
    + Signature(
        color=color(default=None, position=3), tooltip=tooltip(default=None, position=4)
    )
)
def multiscatter(
    data, columns=None, group_by=None, color=None, tooltip=None, height=300, width=400
):
    """Generate many scatter plots.

    Based on several columns, pairwise.
    """
    kwargs = keyfilter(
        lambda x: x in ["color", "tooltip"],
        valfilter(lambda x: x is not None, locals()),
    )
    assert group_by is None, "Long format not supported yet"
    return (
        alt.Chart(data, height=height / len(columns), width=width / len(columns))
        .mark_point(size=1 / len(columns))
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            **kwargs
        )
        .repeat(row=columns, column=columns)
    )
