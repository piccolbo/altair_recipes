"""Collection of signatures used throughout the package."""

from .converters import Column, Columns, to_dataframe, init_cols
from altair import Chart, LayerChart
from autosig import Signature, param, Retval
from functools import partial

recipe = Signature(
    Retval(
        validator=lambda x: isinstance(x, (Chart, LayerChart)),
        docstring="""type altair.Chart or altair.LayerChart
    An altair Chart.""",
    ),
    data=param(
        default=None,
        converter=to_dataframe,
        position=0,
        docstring="""`altair.Data` or `pandas.DataFrame` or csv or json file URL
    The data from which the statistical graphics is being generated""",
    ),
    height=param(
        default=600,
        converter=int,
        position=-2,
        docstring="""`int`
    The height of the chart""",
    ),
    width=param(
        default=800,
        converter=int,
        position=-1,
        docstring="""`int`
    The width of the chart""",
    ),
).set_late_init(init_cols)

column = partial(param, converter=Column)

univariate_recipe = recipe + Signature(
    column=column(
        default=0,
        position=1,
        docstring="""`int`, `str`, pandas `Series` or a type convertible to it.
    The column containing the data to be used in the graphics""",
    )
)

bivariate_recipe = recipe + Signature(
    x=column(
        default=0,
        position=1,
        docstring="""`int`, `str`, pandas `Series` or a type convertible to it.
    The column containing the data associated with the horizontal dimension""",
    ),
    y=column(
        default=1,
        position=2,
        docstring="""`int`, `str`, pandas `Series` or a type convertible to it.
    The column containing the data associated with the vertical dimension""",
    ),
)

multivariate_recipe = recipe + Signature(
    columns=param(
        default=None,
        converter=Columns,
        position=1,
        docstring="""collection of: `int`, `str`, pandas `Series` or a type convertible to it.
    The column or columns to be used in the graphics, defaults to all""",
    ),
    group_by=column(
        default=None,
        position=2,
        docstring="""`int`, `str`, pandas `Series` or a type convertible to it.
    The column to be used to group the data when in long form. When group_by is
    specified columns should contain a single column""",
    ),
)

color = partial(
    column,
    docstring="""`str` or `int`
    The column containing the data associated with the color of the mark""",
)

use_color = partial(
    param,
    default=False,
    converter=bool,
    docstring="""bool
    Whether to also use color to encode the same data as the x coordinate""",
)

opacity = partial(
    param,
    default=1,
    converter=float,
    docstring="""float
    The value of the constant opacity of the mark (use to counter overlap)""",
)

tooltip = partial(
    column,
    docstring="""`str` or `int`
    The column containing the data associated with the tooltip text""",
)
