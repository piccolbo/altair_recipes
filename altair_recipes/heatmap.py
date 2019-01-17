"""Heatmap implementation."""
from .common import hue_scale_dark, hue_scale_light
from .signatures import bivariate_recipe, color, column
import altair as alt
from autosig import autosig, Signature, param
from math import sqrt


def maxbins(data):
    """Return a pair of ints with reasonable defaults for binning in heatmap."""
    n = sqrt(data.shape[0])

    return data, n * 4 // 3, n * 3 // 4


@autosig(
    bivariate_recipe
    + Signature(
        color=color(default=2, position=3),
        opacity=column(
            default=None,
            position=4,
            docstring="""`str`
The column containing the data that determines opacity of the mark""",
        ),
        aggregate=param(
            default="average",
            converter=str,
            position=5,
            docstring="""`str`
    The aggregation function to set the color of each mark, see https://altair-viz.github.io/user_guide/encoding.html#encoding-aggregates for available options""",
        ),
    )
)
def heatmap(
    data, x=0, y=1, color=2, opacity=None, aggregate="average", height=600, width=800
):
    """Generate a heatmap."""
    data, nx, ny = maxbins(data)
    if color is None:
        color = ""
        aggregate = "count"
    color = alt.Color(
        aggregate + "(" + color + "):Q",
        scale=hue_scale_dark if opacity is not None else hue_scale_light,
    )
    enc_opt_args = dict(opacity=opacity) if opacity is not None else dict()
    return (
        alt.Chart(data, height=height, width=width)
        .mark_rect()
        .encode(
            x=alt.X(x, bin=alt.Bin(maxbins=nx)),
            y=alt.Y(y, bin=alt.Bin(maxbins=ny)),
            color=color,
            **enc_opt_args,
        )
    )
