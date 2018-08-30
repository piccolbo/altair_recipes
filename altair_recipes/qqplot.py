"""Generate qqplots."""
from .signatures import BivariateRecipe
import altair as alt
from autosig import autosig
import numpy as np


@autosig(BivariateRecipe)
def qqplot(data, x=0, y=1):
    """Generate a quantile-quantile plot."""
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data).mark_point().encode(x=x, y=y)
