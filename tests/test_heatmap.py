import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd

# Compute x^2 + y^2 across a 2D grid
x, y = np.meshgrid(range(-5, 5), range(-5, 5))
z = x**2 + y**2

# Convert this grid to columnar data expected by Altair
data = pd.DataFrame({'x': x.ravel(), 'y': y.ravel(), 'z': z.ravel()})


@viz_reg_test
def test_heatmap():
    return ar.heatmap(data, x='x', y='y', color='z')
