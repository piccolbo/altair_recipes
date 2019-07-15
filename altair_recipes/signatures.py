"""Collection of signatures used throughout the package."""

from .common import to_dataframe, to_column, to_columns
from autosig import Signature, param
from functools import partial

recipe = Signature(
    data=param(
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
)

column = partial(param, validator=to_column)

univariate_recipe = recipe + Signature(
    column=column(
        default=0,
        position=1,
        docstring="""`str` or `int`
    The column containing the data to be used in the graphics""",
    )
)

bivariate_recipe = recipe + Signature(
    x=column(
        default=0,
        position=1,
        docstring="""`str` or `int`
    The column containing the data associated with the horizontal dimension""",
    ),
    y=column(
        default=1,
        position=2,
        docstring="""`str` or `int`
    The column containing the data associated with the vertical dimension""",
    ),
)

multivariate_recipe = recipe + Signature(
    columns=param(
        default=None,
        validator=to_columns,
        position=1,
        docstring="""`str` or `int` or `list` thereof
    The column or columns to be used in the graphics, defaults to all""",
    ),
    group_by=column(
        default=None,
        position=2,
        docstring="""`str` or `int`
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""",
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
