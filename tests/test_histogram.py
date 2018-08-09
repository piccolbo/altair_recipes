import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd
from vega_datasets import data


@viz_reg_test
def test_histogram():
    return ar.histogram(data.movies(), "IMDB_Rating")


@viz_reg_test
def test_layered_histogram():
    df = pd.DataFrame({
        'Trial A': np.random.normal(0, 0.8, 1000),
        'Trial B': np.random.normal(-2, 1, 1000),
        'Trial C': np.random.normal(3, 2, 1000)
    })
    return ar.layered_histogram(df, ["Trial A", "Trial B", "Trial C"])
