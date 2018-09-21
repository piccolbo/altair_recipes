from .common import to_dataframe
from autosig import Signature, param
from functools import partial


def to_column(inst, attribute, value):
    if value is not None:
        value = inst.data.columns[value] if isinstance(value, int) else value
    assert isinstance(value, str) or value is None
    setattr(inst, attribute.name, value)


def to_columns(inst, attribute, value):
    value = (list(inst.data.columns) if value is None else
             ([inst.data.columns[value]] if isinstance(value, int) else
              ([value] if isinstance(value, str) else\
               list(
                  map(lambda x: inst.data.columns[x] if type(x) is int else x,
                      value)))))

    setattr(inst, attribute.name, value)


recipe = Signature(
    data=param(
        converter=to_dataframe,
        position=0,
        docstring="""`altair.Data` or `pandas.DataFrame` or csv or json file URL
    The data from which the statistical graphics is being generated""",
    ))

univariate_recipe = recipe + Signature(
    column=param(
        default=0,
        validator=to_column,
        position=1,
        docstring="""`str` or `int`
    The column containing the data to be used in the graphics""",
    ))

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
    ))

multivariate_recipe = recipe + Signature(
    columns=param(
        default=None,
        validator=to_columns,
        position=2,
        docstring="""`str` or `int` or `list` thereof
    The column or columns to be used in the graphics, defaults to all""",
    ),
    group_by=param(
        default=None,
        validator=to_column,
        position=3,
        docstring="""`str` or `int`
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""",
    ))

color = partial(
    param,
    validator=to_column,
    docstring="""`str` or `int`
The column containing the data associated with the color of the mark""")

tooltip = partial(
    param,
    validator=to_column,
    docstring="""`str` or `int`
The column containing the data associated with the tooltip text""")
