import altair_recipes as ar
from altair_recipes.common import viz_reg_test, gather
from altair_recipes.display_altair import show_test
import numpy as np
import pandas as pd
from vega_datasets import data

#' <h2>Histogram</h2>

#+ results='raw'


@viz_reg_test
def test_histogram():
    return ar.histogram(data.movies(), column="IMDB_Rating")


show_test(test_histogram)
#' <h2>Layered Histogram from wide data</h2>

#+ results='raw'


@viz_reg_test
def test_layered_histogram_wide():
    np.random.seed(0)
    df = pd.DataFrame({
        'Trial A': np.random.normal(0, 0.8, 1000),
        'Trial B': np.random.normal(-2, 1, 1000),
        'Trial C': np.random.normal(3, 2, 1000)
    })
    return ar.layered_histogram(df, columns=["Trial A", "Trial B", "Trial C"])


show_test(test_layered_histogram_wide)

#' <h2>Layered Histogram from long data</h2>

#+ results='raw'


@viz_reg_test
def test_layered_histogram_long():
    np.random.seed(0)
    data = pd.DataFrame({
        'Trial A': np.random.normal(0, 0.8, 1000),
        'Trial B': np.random.normal(-2, 1, 1000),
        'Trial C': np.random.normal(3, 2, 1000)
    })
    columns = list(data.columns)

    ldata = gather(data, key="key", value="value", columns=columns)
    return ar.layered_histogram(ldata, columns="value", group_by="key")


show_test(test_layered_histogram_long)
