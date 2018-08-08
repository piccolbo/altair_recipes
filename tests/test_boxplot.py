import pandas as pd
from vega_datasets import data
import altair_recipes as vs

iris = data.iris()
vs.boxplot(iris, "species", "petalLength")
iris.columns.name = "vars"

vs.boxplot(iris, pd.Series(["petalLength", "sepalLength"], name="lengths"),
           "length")
