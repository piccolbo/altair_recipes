import numpy as np
import pandas as pd
import altair_recipes as vs

df = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.uniform(3, 2, 1000)
})

vs.qqplot(df, x='Trial A', y='Trial C')
