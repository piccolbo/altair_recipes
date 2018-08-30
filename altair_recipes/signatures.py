from .common import to_dataframe
from autosig import signature, Signature, param


@signature
class Recipe(Signature):
    def to_column(self, attribute):
        x = getattr(self, attribute)
        setattr(self, attribute, self.data.columns[x] if type(x) is int else x)
        return getattr(self, attribute)

    def to_columns(self, attribute):
        xx = getattr(self, attribute)
        setattr(
            self,
            attribute,
            list(self.data.columns)
            if xx is None
            else (
                [self.to_column(attribute)]
                if isinstance(xx, (int, str))
                else list(
                    map(lambda x: self.data.columns[x] if type(x) is int else x, xx))))  # yapf: disable

    data = param(
        converter=to_dataframe,
        docstring="""`altair.Data` or `pandas.DataFrame` or csv or json file URL
    The data from which the statistical graphics is being generated""")


@signature
class UnivariateRecipe(Recipe):
    column = param(
        default=0,
        docstring="""`str` or `int`
    The column containing the data to be used in the graphics""")

    def default(self):
        super().default()
        self.to_column("column")


@signature
class BivariateRecipe(Recipe):
    x = param(
        default=0,
        docstring="""`str` or `int`
    The column containing the data associated with the horizontal dimension""")
    y = param(
        default=1,
        docstring="""`str` or `int`
    The column containing the data associated with the vertical dimension""")

    def default(self):
        super().default()
        for attribute in ["x", "y"]:
            self.to_column(attribute)


@signature
class MultivariateRecipe(Recipe):
    columns = param(
        None,
        docstring="""`str` or `int` or `list` thereof
    The column or columns to be used in the graphics, defaults to all""")
    group_by = param(
        default=None,
        docstring="""`str` or `int`
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""")

    def default(self):
        super().default()
        self.to_columns("columns")
        self.to_column("group_by")
