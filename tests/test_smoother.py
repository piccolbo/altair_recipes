"""Test smoother."""
import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
import numpy as np
import pandas as pd

# fmt: off
#' <h2>Smoother</h2>
# fmt: on


@viz_reg_test
def test_smoother():
    np.random.seed(0)
    x = np.random.uniform(size=100)
    data = pd.DataFrame(dict(x=x, y=np.random.uniform(size=100) + 10 * x))
    return ar.smoother(data, *list(data.columns))


show_test(test_smoother)
