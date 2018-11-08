"""Scatter plots."""
from .signatures import bivariate_recipe, multivariate_recipe, color, tooltip
import altair as alt
from autosig import autosig, Signature
from .common import choose_kwargs


scatter_sig = Signature(
    color=color(default=None, position=3), tooltip=tooltip(default=None, position=4)
)


@autosig(bivariate_recipe + scatter_sig)
def scatter(data, x=0, y=1, color=None, tooltip=None, height=300, width=400):
    """Generate a scatter plot."""
    kwargs = choose_kwargs(from_=locals(), which=["color", "tooltip"])
    return (
        alt.Chart(data, height=height, width=width)
        .mark_point()
        .encode(x=x, y=y, **kwargs)
    )


@autosig(multivariate_recipe + scatter_sig)
def multiscatter(
    data, columns=None, group_by=None, color=None, tooltip=None, height=300, width=400
):
    """Generate many scatter plots.

    Based on several columns, pairwise.
    """
    kwargs = choose_kwargs(from_=locals(), which=["color", "tooltip"])

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
