import altair as alt
from autosig import signature, Signature, param
import pandas as pd


@signature
class Recipe(Signature):
    data = param()
    mark = param(default={}, convert=dict)
    encoding = param(default={}, convert=dict)
    properties = param(default={}, convert=dict)


@signature
class UnivariateRecipe(Recipe):
    column = param(default=0)


@signature
class BivariateRecipe(Recipe):
    x = param(default="x")
    y = param(default="y")


@signature
class MultivariateRecipe(Recipe):
    columns = param(default=None)
    group_by = param(default=None)

    def validate(self):
        if self.columns is None: columns = list(self.data.columns)


def viz_reg_test(test_f):
    def fun(regtest):
        plot = test_f()
        if regtest is not None:
            regtest.write(plot.to_json())
        plot.save(
            test_f.__code__.co_filename + "_" + test_f.__qualname__ + ".html")
        return plot

    return fun


def to_dataframe(data):
    #this is an undocumented hack
    return alt.Chart(data).data


def default(*args):
    return next(x for x in args if x is not None)


# unused should kill?
# def update(d1, d2):
#     d1.update(d2)
#     return d1


def gather(data, key, value, columns):
    return pd.melt(
        data,
        id_vars=[col for col in data.columns if col not in columns],
        value_vars=columns,
        var_name=key,
        value_name=value)
