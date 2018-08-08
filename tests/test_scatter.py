from vega_datasets import data
import altair_recipes as ar

ar.scatter(
    data.iris(),
    x="petalWidth",
    y='petalLength',
    color="sepalWidth",
    tooltip="species")

ar.multiscatter(data.iris())
ar.multiscatter(
    data.iris(), variables=data.iris().columns[:-1], color="species")
