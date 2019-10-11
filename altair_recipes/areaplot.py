"""areaplots."""
from common import warn_not_distinct
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature, param
from logging import warning
from enum import Enum


StackType = Enum("StackType", "true false  normalize")


@autosig(
    bivariate_recipe
    + Signature(
        color(default=2, position=3),
        stack=param(
            default=None,
            position=4,
            converter=lambda x: StackType(x) if x is not None else x,
        ),
    )
)
def areaplot(data=None, x=0, y=1, color=2, stack=None, height=600, width=800):
    """Generate a areaplot."""
    warn_not_distinct(data[x])
    if len(set(data[x])) != len(data[x]):
        warning("The relation to plot is not a function")
    if stack is not None:
        x = alt.X(x=x, stack=stack.name)
    return alt.Chart(data=data, height=height, width=width).mark_area().encode(x=x, y=y)
