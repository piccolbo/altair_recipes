import altair as alt
import numpy as np
import pandas as pd


def autocorrelation(data, variable, max_lag=None):
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[variable].autocorr(lag=lag)
                             for lag in lags]))
    return alt.Chart(_data).mark_bar().encode(
        x="Lag:O", y="Autocorrelation" + ":Q")
