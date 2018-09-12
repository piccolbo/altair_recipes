import altair_recipes as ar
from altair_recipes.common import viz_reg_test
import numpy as np
import pandas as pd
from vega_datasets import data
from altair_recipes.display_altair import display_altair_chart


#' ## Test Heatmap
@viz_reg_test
def test_heatmap():
    # Compute x^2 + y^2 across a 2D grid
    x, y = np.meshgrid(range(-5, 6), range(-5, 6))
    z = x**2 + y**2

    # Convert this grid to columnar data expected by Altair
    data = pd.DataFrame({'x': x.ravel(), 'y': y.ravel(), 'z': z.ravel()})

    return ar.heatmap(data, x='x', y='y', color='z')


#+ results='raw'
display_altair_chart(test_heatmap(None))

#' ## Test Count Heatmap


@viz_reg_test
def test_count_heatmap():
    source = data.movies.url
    return ar.count_heatmap(
        source, x='IMDB_Rating', y='Rotten_Tomatoes_Rating')


#+ results='raw'
display_altair_chart(test_count_heatmap(None))
