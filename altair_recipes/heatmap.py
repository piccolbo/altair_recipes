"""Heatmap implementation."""
import altair as alt
from .docstrings import make_docstring
from .common import update_kwargs as uk, to_dataframe
from math import sqrt


def heatmap(data, x, y, color, mark={}, encoding={}, properties={}):
    """See below."""
    data = to_dataframe(data)
    nrow = data.shape[0]
    return alt.Chart(data).mark_rect(**mark).encode(**uk(
        x=alt.X(x + ':Q', bin=alt.Bin(maxbins=3 * sqrt(nrow / 18))),
        y=alt.Y(y + ':Q', bin=alt.Bin(maxbins=2 * sqrt(nrow / 18))),
        color=alt.Color(
            'average(' + color + '):Q', scale=alt.Scale(scheme='greenblue')),
        updates=encoding)).properties(**properties)


heatmap.__doc__ = make_docstring(
    heatmap,
    """Generate a heatmap.""",
    additional_params=dict(color="""color: `str` or other column selector
    The color to be used at each `(x,y)` location"""))


def binned_heatmap(data, x, y, mark={}, encoding={}, properties={}):
    """See below."""
    data = to_dataframe(data)
    nrow = data.shape[0]
    return alt.Chart(data).mark_rect(**mark).encode(**uk(
        x=alt.X(x + ':Q', bin=alt.Bin(maxbins=3 * sqrt(nrow / 18))),
        y=alt.Y(y + ':Q', bin=alt.Bin(maxbins=2 * sqrt(nrow / 18))),
        color=alt.Color(
            'count(' + x + '):Q', scale=alt.Scale(scheme='greenblue')),
        updates=encoding)).properties(**properties)


heatmap.__doc__ = make_docstring(
    binned_heatmap,
    summary="Create a heatmap of the count of points in each square")
