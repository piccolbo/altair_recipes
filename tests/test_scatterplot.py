import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_pweave import show_test
from vega_datasets import data


#' <h2>scatterplot</h2>


@viz_reg_test
def test_scatterplot():
    return ar.scatterplot(
        data.iris(),
        x="petalWidth",
        y="petalLength",
        color="sepalWidth",
        tooltip="species",
    )


show_test(test_scatterplot)


#' <h2>Multiscatterplot at defaults</h2>


@viz_reg_test
def test_multiscatterplot_defaults():
    return ar.multiscatterplot(data.iris())


show_test(test_multiscatterplot_defaults)


#' <h2>Multiscatterplot with explicit parameters</h2>


@viz_reg_test
def test_multiscatterplot_args():
    """Test multiscatterplot."""
    return ar.multiscatterplot(
        data.iris(), columns=data.iris().columns[:-1], color="species"
    )


show_test(test_multiscatterplot_args)
