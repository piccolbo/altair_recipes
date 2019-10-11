import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_pweave import show_test
from vega_datasets import data

#' <h2>Areaplot</h2>


@viz_reg_test
def test_areaplot():
    return ar.areaplot(
        data.iowa_electricity(), x="year", y="net_generation", color="source"
    )


show_test(test_areaplot)
