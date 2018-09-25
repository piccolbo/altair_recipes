"""Autocorrelation plot."""
from .signatures import univariate_recipe
import altair as alt
from autosig import autosig, Signature, param
import numpy as np
import pandas as pd


@autosig(
    univariate_recipe
    + Signature(
        max_lag=param(
            default=None,
            position=2,
            docstring="""int
    Maximum lag to show in the plot, defaults to number of rows in data""",
        )
    )
)
def autocorrelation(data, column=0, max_lag=None, height=300, width=400):
    """Generate an autocorrelation plot."""
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(Lag=lags, Autocorrelation=[data[column].autocorr(lag=lag) for lag in lags])
    )
    return (
        alt.Chart(_data, height=height, width=width)
        .mark_bar()
        .encode(x="Lag:O", y="Autocorrelation" + ":Q")
    )
