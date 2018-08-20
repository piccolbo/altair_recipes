"""Test smoother."""
import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd


@viz_reg_test
def test_smoother():
    """Test smoother."""
    np.random.seed(0)
    x = np.random.uniform(size=100)
    data = pd.DataFrame(dict(x=x, y=np.random.uniform(size=100) + 10 * x))
    return ar.smoother(data, *list(data.columns))
