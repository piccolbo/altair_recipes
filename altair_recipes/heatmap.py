"""Heatmap implementation."""
from .docstrings import make_docstring
from .signatures import BivariateRecipe
import altair as alt
from autosig import autosig, signature, param
from math import sqrt


def heatmap_preprocess(data, x, y):
    nx = sqrt(data.shape[0])
    ny = nx
    return data, nx, ny


@signature
class Heatmap(BivariateRecipe):
    color = param(default=3)

    def __attrs_post_init__(self):
        self.to_column("color")


@autosig(Heatmap)
def heatmap(
        data,
        x=0,
        y=1,
        color=3,
):
    """See below."""
    data, nx, ny = heatmap_preprocess(data, x, y)
    return alt.Chart(data).mark_rect().encode(
        x=alt.X(x + ':Q', bin=alt.Bin(maxbins=nx)),
        y=alt.Y(y + ':Q', bin=alt.Bin(maxbins=ny)),
        color=alt.Color(
            'average(' + color + '):Q', scale=alt.Scale(scheme='greenblue')))


heatmap.__doc__ = make_docstring(
    heatmap,
    """Generate a heatmap.""",
    additional_params=dict(color="""color: `str` or other column selector
    The color to be used at each `(x,y)` location"""))


@autosig(BivariateRecipe)
def binned_heatmap(
        data,
        x=0,
        y=1,
):
    """See below."""
    data, nx, ny = heatmap_preprocess(data, x, y)
    return alt.Chart(data).mark_rect().encode(
        x=alt.X(x + ':Q', bin=alt.Bin(maxbins=nx)),
        y=alt.Y(y + ':Q', bin=alt.Bin(maxbins=ny)),
        color=alt.Color(
            'count(' + x + '):Q', scale=alt.Scale(scheme='greenblue')))


heatmap.__doc__ = make_docstring(
    binned_heatmap,
    summary="Create a heatmap of the count of points in each square")
