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
    """Short summary.

    Parameters
    ----------
    data : type
        Description of parameter `data`.
    column : type
        Description of parameter `column`.
    max_lag : type
        Description of parameter `max_lag`.
    mark : type
        Description of parameter `mark`.
    encoding : type
        Description of parameter `encoding`.
    properties : type
        Description of parameter `properties`.

    Returns
    -------
    type
        Description of returned object.

    """
    data = to_dataframe(data)
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    if type(column) is int:
        column = data.columns[column]
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[column].autocorr(lag=lag) for lag in lags]))
    return alt.Chart(_data).mark_bar(**mark).encode(
        x="Lag:O", y="Autocorrelation" + ":Q",
        **encoding).properties(**properties)
