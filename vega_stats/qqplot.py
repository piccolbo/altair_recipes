import altair as alt
import numpy as np


def qqplot(data, x="x", y="y"):
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data).mark_point().encode(x=x, y=y)
