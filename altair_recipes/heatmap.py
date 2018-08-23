"""Heatmap implementation."""
import altair as alt
from .docstrings import make_docstring
from .common import to_dataframe
from math import sqrt


def heatmap_preprocess(data, x, y):
    data = to_dataframe(data)
    nx = sqrt(data.shape[0])
    ny = nx
    return data, nx, ny


def heatmap(
        data,
        x,
        y,
        color,
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


def binned_heatmap(
        data,
        x,
        y,
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
