import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from vega_datasets import data


@viz_reg_test
def test_scatter():
    return ar.scatter(
        data.iris(),
        x="petalWidth",
        y='petalLength',
        color="sepalWidth",
        tooltip="species")


@viz_reg_test
def test_multiscatter_defaults():
    return ar.multiscatter(data.iris())


@viz_reg_test
def test_multiscatter_args():
    return ar.multiscatter(
        data.iris(), columns=data.iris().columns[:-1], color="species")
