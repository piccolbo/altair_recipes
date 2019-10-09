"""Lineplots."""

from .signatures import bivariate_recipe
import altair as alt
from autosig import autosig
from logging import warning


@autosig(bivariate_recipe)
def lineplot(data=None, x=0, y=1, height=600, width=800):
    """Generate a lineplot."""
    if len(set(data[x])) != len(data[x]):
        warning("The relation to plot is not a function")
    return alt.Chart(data=data, height=height, width=width).mark_line().encode(x=x, y=y)
