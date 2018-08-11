import altair as alt
import numpy as np
from altair_recipes.common import to_dataframe


def qqplot(data, x="x", y="y", mark={}, encoding={}, properties={}):
    data = to_dataframe(data)
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data).mark_point(**mark).encode(
        x=x, y=y, **encoding).properties(**properties)
