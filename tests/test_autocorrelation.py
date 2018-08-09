import numpy as np
import pandas as pd
import altair_recipes as ar


def test_autocorrelation():
    data = pd.DataFrame(dict(x=np.random.uniform(size=100)))
    return ar.autocorrelation(data, "x", max_lag=15)
