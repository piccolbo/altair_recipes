"""Autocorrelation plot."""
import altair as alt
import numpy as np
import pandas as pd
from .common import to_dataframe
from .docstrings import make_docstring


def autocorrelation(data,
                    column,
                    max_lag=None,
                    mark={},
                    encoding={},
                    properties={}):
    """See below."""
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


autocorrelation.__doc__ = make_docstring(
    autocorrelation,
    summary="Generate an autocorrelation plot",
    additional_params=dict(max_lag="""max_lag: int
    Maximum lag to show in the plot, default to number of rows in data"""))
