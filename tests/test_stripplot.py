import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
import numpy as np
import pandas as pd


#' <h2>Stripplot</h2>


@viz_reg_test
def test_stripplot():
    x = np.array(range(100)) // 10
    data = pd.DataFrame(dict(x=x, y=np.random.normal(size=len(x))))

    return ar.stripplot(data)


show_test(test_stripplot)
