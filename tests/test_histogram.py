import numpy as np
import pandas as pd
from vega_datasets import data
import altair_recipes as ar

source = data.movies()

ar.histogram(source, "IMDB_Rating")

df = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

ar.layered_histogram(df, ["Trial A", "Trial B", "Trial C"])
