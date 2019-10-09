import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_pweave import show_test
from hypothesis import given
from hypothesis.extra.pandas import columns, data_frames
from vega_datasets import data


#' <h2>Scatterplot</h2>


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


#'<h2>Scatterplot alternate data syntax</h2>


@viz_reg_test
def test_scatterplot_alternate_data():
    d = data.iris()
    return ar.scatterplot(
        x=d["petalWidth"],
        y=d["petalLength"],
        color=d["sepalWidth"],
        tooltip=d["species"],
    )


show_test(test_scatterplot_alternate_data)

#' A randomized test of equivalence between the two data syntaxes:


@given(data=data_frames(columns=columns(["a", "b", "c"], dtype=float)))
def test_scatterplot_series(data):
    chart1 = ar.scatterplot(data=data[["a", "c"]])
    chart2 = ar.scatterplot(x=data["a"], y=data["c"])
    assert chart1.to_dict() == chart2.to_dict()


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


#' <h2>Multiscatterplot alternate data syntax</h2>


@viz_reg_test
def test_multiscatterplot_args_alternate():
    """Test multiscatterplot."""
    d = data.iris()
    return ar.multiscatterplot(
        columns=[d["sepalLength"], d["sepalWidth"], d["petalLength"]],
        color=d["species"],
    )


show_test(test_multiscatterplot_args_alternate)


#' A randomized test of equivalence bewteen the two
@given(data=data_frames(columns=columns(["a", "b", "c"], dtype=float)))
def test_multiscatterplot_series(data):
    chart1 = ar.multiscatterplot(data=data)
    chart2 = ar.multiscatterplot(columns=[data["a"], data["b"], data["c"]])
    assert chart1.to_dict() == chart2.to_dict()
