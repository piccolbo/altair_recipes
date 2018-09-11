"""Heatmap implementation."""
from .signatures import BivariateRecipe
import altair as alt
from autosig import autosig, signature, param
from math import sqrt


def maxbins(data):
    n = sqrt(data.shape[0])

    return data, n * 4 // 3, n * 3 // 4


@signature
class Heatmap(BivariateRecipe):
    color = param(
        default=3,
        docstring="""`str` or `int`
    The color to be used at each `(x,y)` location""")
    aggregate = param(
        default="average",
        docstring="""`str`
    The aggregation function to set the color of each mark, see https://altair-viz.github.io/user_guide/encoding.html#encoding-aggregates for available options"""
    )

    def default(self):
        super().default()
        self.to_column("color")


@autosig(Heatmap)
def heatmap(data, x=0, y=1, color=3, aggregate='average'):
    """Generate a heatmap."""
    data, nx, ny = maxbins(data)
    return alt.Chart(data).mark_rect().encode(
        x=alt.X(x, bin=alt.Bin(maxbins=nx)),
        y=alt.Y(y, bin=alt.Bin(maxbins=ny)),
        color=alt.Color(
            aggregate + '(' + color + '):Q',
            scale=alt.Scale(scheme='greenblue')))


@autosig(BivariateRecipe)
def count_heatmap(
        data,
        x=0,
        y=1,
):
    """Create a heatmap of the count of points in each square."""
    return heatmap(data, x=x, y=y, color='x', aggregate='count')
