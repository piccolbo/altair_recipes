from .common import to_dataframe, UnivariateRecipe
import altair as alt
from autosig import autosig, signature, param
import numpy as np
import pandas as pd


@signature
class Autocorrelation(UnivariateRecipe):
    max_lag = param(default=None)


@autosig(Autocorrelation)
def autocorrelation(data,
                    column=0,
                    max_lag=None,
                    mark={},
                    encoding={},
                    properties={}):
    data = to_dataframe(data)
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    if type(column) is int:
        column = data.columns[0]
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[column].autocorr(lag=lag) for lag in lags]))
    return alt.Chart(_data).mark_bar(**mark).encode(
        x="Lag:O", y="Autocorrelation" + ":Q",
        **encoding).properties(**properties)
