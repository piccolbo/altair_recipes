import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
import numpy as np
import pandas as pd
from vega_datasets import data

# fmt: off
#' <h2>Heatmap</h2>
# fmt: on


@viz_reg_test
def test_heatmap():
    # Compute x^2 + y^2 across a 2D grid
    x, y = np.meshgrid(range(-5, 6), range(-5, 6))
    z = x ** 2 + y ** 2

    # Convert this grid to columnar data expected by Altair
    data = pd.DataFrame({"x": x.ravel(), "y": y.ravel(), "z": z.ravel()})

    return ar.heatmap(data, x="x", y="y", color="z")


show_test(test_heatmap)

# fmt: off
#' <h2>Count Heatmap</h2>
# fmt: on


@viz_reg_test
def test_count_heatmap():
    source = data.movies.url
    return ar.count_heatmap(source, x="IMDB_Rating", y="Rotten_Tomatoes_Rating")


show_test(test_count_heatmap)
