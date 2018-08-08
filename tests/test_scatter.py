from vega_datasets import data
import vega_stats as vs

vs.scatter(
    data.iris(),
    x="petalWidth",
    y='petalLength',
    color="sepalWidth",
    tooltip="species")

vs.multiscatter(data.iris())
vs.multiscatter(
    data.iris(), variables=data.iris().columns[:-1], color="species")
