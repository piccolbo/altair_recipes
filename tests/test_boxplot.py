import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from vega_datasets import data


@viz_reg_test
def test_boxplot_melted():
    return ar.boxplot(data.iris(), columns="petalLength", group_by="species")


@viz_reg_test
def test_boxplot_cast():
    iris = data.iris()
    return ar.boxplot(iris, columns=list(iris.columns[:-1]))
