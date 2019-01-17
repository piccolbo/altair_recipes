import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
from vega_datasets import data

#' <h2>Barchart</h2>


@viz_reg_test
def test_barchart_color():
    source = data.barley()
    return ar.barchart(source, x="year:O", y="mean(yield)", hfacet="site")


show_test(test_barchart_color)
