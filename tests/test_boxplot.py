import pandas as pd
from vega_datasets import data
import vega_stats as vs

iris = data.iris()
vs.boxplot(iris, "species", "petalLength")
iris.columns.name = "vars"

vs.boxplot(iris, pd.Series(["petalLength", "sepalLength"], name="lengths"),
           "length")
