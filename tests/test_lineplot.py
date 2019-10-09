import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_pweave import show_test
from vega_datasets import data

#' <h2>Lineplot</h2>


@viz_reg_test
def test_lineplot():
    return ar.lineplot(data.iris(), x="petalWidth", y="petalLength")


show_test(test_lineplot)
