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
        default=300,
        converter=int,
        position=-2,
        docstring="""`int`
    The height of the chart""",
    ),
    width=param(
        default=400,
        converter=int,
        position=-1,
        docstring="""`int`
    The height of the chart""",
    ),
)

univariate_recipe = recipe + Signature(
    column=param(
        default=0,
        validator=to_column,
        position=1,
        docstring="""`str` or `int`
    The column containing the data to be used in the graphics""",
    )
)

bivariate_recipe = recipe + Signature(
    x=param(
        default=0,
        validator=to_column,
        position=1,
        docstring="""`str` or `int`
    The column containing the data associated with the horizontal dimension""",
    ),
    y=param(
        default=1,
        validator=to_column,
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
    group_by=param(
        default=None,
        validator=to_column,
        position=2,
        docstring="""`str` or `int`
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""",
    ),
)

color = partial(
    param,
    validator=to_column,
    docstring="""`str` or `int`
The column containing the data associated with the color of the mark""",
)

tooltip = partial(
    param,
    validator=to_column,
    docstring="""`str` or `int`
The column containing the data associated with the tooltip text""",
)
