"""Heatmap implementation."""
import altair as alt
from .docstrings import make_docstring


def heatmap(data, x, y, color, mark={}, encoding={}, properties={}):
    """See below"""
    return alt.Chart(data).mark_rect().encode(x='x:O', y='y:O', color='z:Q')


heatmap.__doc__ = make_docstring(
    heatmap,
    """Generate a heatmap.""",
    additional_params=dict(color="""color: `str` or other column selector
    The color to be used at each `(x,y)` location"""))
