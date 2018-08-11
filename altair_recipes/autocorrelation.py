import altair as alt
import numpy as np
import pandas as pd
from altair_recipes.common import to_dataframe


def autocorrelation(data,
                    column,
                    max_lag=None,
                    mark={},
                    encoding={},
                    properties={}):
    data = to_dataframe(data)
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[column].autocorr(lag=lag) for lag in lags]))
    return alt.Chart(_data).mark_bar(**mark).encode(
        x="Lag:O", y="Autocorrelation" + ":Q",
        **encoding).properties(**properties)