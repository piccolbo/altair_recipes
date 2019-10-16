"""Lineplots."""
from .common import warn_not_distinct, choose_kwargs
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature


@autosig(bivariate_recipe + Signature(color=color(default=None, position=3)))
def lineplot(data=None, x=0, y=1, color=None, height=600, width=800):
    """Generate a lineplot."""
    warn_not_distinct(data, x, color)
    opt_args = choose_kwargs(locals(), ["color"])
    return (
        alt.Chart(data=data, height=height, width=width)
        .encode(x=x, y=y, **opt_args)
        .mark_line()
    )
