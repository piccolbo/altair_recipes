import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import pandas as pd
from vega_datasets import data


@viz_reg_test
def test_boxplot_melted():
    return ar.boxplot(data.iris(), "petalLength", "species")


@viz_reg_test
def test_boxplot_cast():
    iris = data.iris()
    iris.columns.name = "vars"
    return ar.boxplot(iris,
                      pd.Series(
                          ["petalLength", "sepalLength"], name="lengths"),
                      "length")
