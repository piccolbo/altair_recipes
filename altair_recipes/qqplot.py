"""Generate qqplots."""
from .signatures import bivariate_recipe
import altair as alt
from autosig import autosig
import numpy as np


@autosig(bivariate_recipe)
def qqplot(data, x=0, y=1, height=300, width=400):
    """Generate a quantile-quantile plot."""
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data, height=height, width=width).mark_point().encode(x=x, y=y)
