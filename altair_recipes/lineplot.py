"""Lineplots."""
from .common import warn_not_distinct
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature


@autosig(bivariate_recipe + Signature(color=color(default=2, position=3)))
def lineplot(data=None, x=0, y=1, color=2, height=600, width=800):
    """Generate a lineplot."""
    warn_not_distinct(data[x])
    return (
        alt.Chart(data=data, height=height, width=width)
        .encode(x=x, y=y, color=color)
        .mark_line()
    )
