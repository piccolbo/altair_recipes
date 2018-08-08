import altair as alt
import pandas as pd
import numpy as np


def qqplot(data, x="x", y="y"):
    n = data.shape[0]
    data = data.quantile(np.arange(0, 1, step=10 / n))
    return alt.Chart(data).mark_point().encode(x=x, y=y)


df = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.uniform(3, 2, 1000)
})

qqplot(df, x='Trial A', y='Trial C')
