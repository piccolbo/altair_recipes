"""Scatterplots."""
from .common import choose_kwargs, hue_scale_dark, hue_scale_light
from .signatures import bivariate_recipe, multivariate_recipe, color, tooltip
import altair as alt
from autosig import autosig, Signature, param
from numbers import Number


scatterplot_sig = Signature(
    color=color(default=None, position=3),
    opacity=param(
        default=1,
        position=4,
        converter=float,
        docstring="""`float`
A constant value for the opacity of the mark""",
    ),
    tooltip=tooltip(default=None, position=5),
)


@autosig(bivariate_recipe + scatterplot_sig)
def scatterplot(
    data, x=0, y=1, color=None, opacity=1, tooltip=None, height=600, width=800
):
    """Generate a scatterplot."""
    if color is not None:
        if isinstance(data[color].iloc[0], Number):
            color = alt.Color(
                color, scale=hue_scale_light if opacity == 1 else hue_scale_dark
            )
    kwargs = choose_kwargs(locals(), ["color", "tooltip"])
    return alt.Chart(
        data,
        height=height,
        width=width,
        mark=alt.MarkDef(type="point" if opacity == 1 else "circle", opacity=opacity),
    ).encode(x=x, y=y, **kwargs)


@autosig(multivariate_recipe + scatterplot_sig)
def multiscatterplot(
    data,
    columns=None,
    group_by=None,
    color=None,
    opacity=1,
    tooltip=None,
    height=600,
    width=800,
):
    """Generate many scatterplots.

    Based on several columns, pairwise.
    """
    kwargs = choose_kwargs(from_=locals(), which=["color", "tooltip"])

    assert group_by is None, "Long format not supported yet"
    return (
        alt.Chart(data, height=height // len(columns), width=width // len(columns))
        .mark_point(size=1 / len(columns), opacity=opacity)
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            **kwargs
        )
        .repeat(row=columns, column=columns)
    )
