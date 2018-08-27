"""Generate qqplots."""
from .docstrings import make_docstring
from .signatures import BivariateRecipe
import altair as alt
from autosig import autosig
import numpy as np


@autosig(BivariateRecipe)
def qqplot(data, x=0, y=1):
    """See below."""
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data).mark_point().encode(x=x, y=y)


qqplot.__doc__ = make_docstring(
    qqplot, summary="Generate a quantile-quantile plot")
