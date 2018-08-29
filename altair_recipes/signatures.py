from .common import to_dataframe
from autosig import signature, Signature, param


@signature
class Recipe(Signature):
    def to_column(self, attribute):
        x = getattr(self, attribute)
        setattr(self, attribute, self.data.columns[x] if type(x) is int else x)

    def to_columns(self, attribute):
        xx = getattr(self, attribute)
        setattr(self, attribute, [xx] if isinstance(xx, str) else list(
            map(lambda x: self.data.columns[x] if type(x) is int else x, xx)))

    data = param(converter=to_dataframe)


@signature
class UnivariateRecipe(Recipe):
    column = param(default=0)

    def __attrs_post_init__(self):
        self.to_column("column")


@signature
class BivariateRecipe(Recipe):
    x = param(default=0)
    y = param(default=1)

    def __attrs_post_init__(self):
        for attribute in ['x', 'y']:
            self.to_column(attribute)


@signature
class MultivariateRecipe(Recipe):
    columns = param(None)
    group_by = param(default=None)

    def __attrs_post_init__(self):
        self.to_columns("columns")
        self.to_column("group_by")
