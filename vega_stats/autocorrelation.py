import altair as alt
import pandas as pd
import numpy as np

variable = "x"


def autocorrelation(data, variable, max_lag=None):
    max_lag = max_lag or data.shape[0] - 1
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[variable].autocorr(lag=lag)
                             for lag in lags]))
    return alt.Chart(_data).mark_bar().encode(
        x="Lag:O", y="Autocorrelation" + ":Q")


data = pd.DataFrame(dict(x=np.random.uniform(size=100)))

autocorrelation(data, "x", max_lag=15).mark_bar(color = "grey")
