import numpy as np
import pandas as pd
from vega_datasets import data
import vega_stats as vs

source = data.movies()

vs.histogram(source, "IMDB_Rating")

df = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

vs.layered_histogram(df, ["Trial A", "Trial B", "Trial C"])
