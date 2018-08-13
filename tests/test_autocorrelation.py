import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd


@viz_reg_test
def test_autocorrelation():
    np.random.seed(0)
    data = pd.DataFrame(dict(x=np.random.uniform(size=100)))
    return ar.autocorrelation(data, column="x", max_lag=15)
