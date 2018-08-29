"""Autocorrelation plot."""
from .docstrings import make_docstring
from .signatures import UnivariateRecipe
import altair as alt
from autosig import autosig, signature, param
import numpy as np
import pandas as pd


@signature
class Autocorrelation(UnivariateRecipe):
    max_lag = param(default=None)


@autosig(Autocorrelation)
def autocorrelation(
        data,
        column=0,
        max_lag=None,
):
    """See below."""
    max_lag = data.shape[0] - 1 if max_lag is None else int(max_lag)
    lags = np.arange(0, max_lag + 1)
    _data = pd.DataFrame(
        dict(
            Lag=lags,
            Autocorrelation=[data[column].autocorr(lag=lag) for lag in lags]))
    return alt.Chart(_data).mark_bar().encode(
        x="Lag:O",
        y="Autocorrelation" + ":Q",
    )


autocorrelation.__doc__ = make_docstring(
    autocorrelation,
    summary="Generate an autocorrelation plot",
    additional_params=dict(max_lag="""max_lag: int
    Maximum lag to show in the plot, defaults to number of rows in data"""))
