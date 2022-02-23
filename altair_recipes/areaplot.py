"""areaplots."""
from .common import warn_not_distinct, choose_kwargs
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature, param
from enum import Enum


class StackType(Enum):
    """Type of stacking for areaplot charts.

    Attributes
    ----------
    auto : None
        Automatic stacking.
    true : bool
        Stacked.
    false : bool
        Not stacked.
    normalize : string
        Normalize stacked to 1.

    """

    auto = None  # no, must not pass anything
    true = True
    false = False
    normalize = "normalize"


@autosig(
    bivariate_recipe
    + Signature(
        color=color(default=None, position=3),
        stack=param(
            default=StackType.auto,
            position=4,
            converter=StackType,
            docstring="""StackType
            One of `StackType.auto` (automatic selection), `StackType.true` (force), `StackType.false` (no stacking) and `StackType.normalize` (for normalized stacked)""",
        ),
    )
)
def areaplot(
    data=None, x=0, y=1, color=None, stack=StackType.auto, height=600, width=800
):
    """Generate an areaplot."""
    warn_not_distinct(data, x, color)
    if stack is not StackType.auto:
        y = alt.Y(y, stack=stack.value)
    opt_args = choose_kwargs(locals(), ["color"])
    return (
        alt.Chart(data=data, height=height, width=width)
        .mark_area(opacity=1)
        .encode(x=x, y=y, **opt_args)
    )
