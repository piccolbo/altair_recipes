import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
from vega_datasets import data

#' ##  Scatter
#+ results='raw'


@viz_reg_test
def test_scatter():
    return ar.scatter(
        data.iris(),
        x="petalWidth",
        y='petalLength',
        color="sepalWidth",
        tooltip="species")


show_test(test_scatter)

#' ##  Multiscatter at defaults
#+ results='raw'


@viz_reg_test
def test_multiscatter_defaults():
    return ar.multiscatter(data.iris())


show_test(test_multiscatter_defaults)

#' ##  Multiscatter with explicit parameters
#+ results='raw'


@viz_reg_test
def test_multiscatter_args():
    return ar.multiscatter(
        data.iris(), columns=data.iris().columns[:-1], color="species")


show_test(test_multiscatter_args)
