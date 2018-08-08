import pandas as pd
from vega_datasets import data
import altair_recipes as ar

iris = data.iris()
ar.boxplot(iris, "species", "petalLength")
iris.columns.name = "vars"

ar.boxplot(iris, pd.Series(["petalLength", "sepalLength"], name="lengths"),
           "length")
