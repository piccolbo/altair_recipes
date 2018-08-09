from vega_datasets import data
import altair_recipes as ar


def test_scatter():
    return ar.scatter(
        data.iris(),
        x="petalWidth",
        y='petalLength',
        color="sepalWidth",
        tooltip="species")


def test_multiscatter_defaults():
    return ar.multiscatter(data.iris())


def test_multiscatter_args():
    return ar.multiscatter(
        data.iris(), variables=data.iris().columns[:-1], color="species")
