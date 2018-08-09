import pandas as pd
from vega_datasets import data
import altair_recipes as ar


def test_boxplot_melted():
    return ar.boxplot(data.iris(), "species", "petalLength")


def test_boxplot_cast():
    iris = data.iris()
    iris.columns.name = "vars"
    return ar.boxplot(iris,
                      pd.Series(
                          ["petalLength", "sepalLength"], name="lengths"),
                      "length")
