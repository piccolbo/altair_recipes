import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd


@viz_reg_test
def test_qqplot():
    df = pd.DataFrame({
        'Trial A': np.random.normal(0, 0.8, 1000),
        'Trial B': np.random.normal(-2, 1, 1000),
        'Trial C': np.random.uniform(3, 2, 1000)
    })
    return ar.qqplot(df, x='Trial A', y='Trial C')
