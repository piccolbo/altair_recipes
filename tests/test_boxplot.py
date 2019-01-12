import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
from vega_datasets import data


#' <h2>Boxplot from melted data</h2>


@viz_reg_test
def test_boxplot_melted():
    return ar.boxplot(data.iris(), columns="petalLength", group_by="species")


show_test(test_boxplot_melted)


#' <h2>Boxplot from cast data</h2>


@viz_reg_test
def test_boxplot_cast():
    iris = data.iris()
    return ar.boxplot(iris, columns=list(iris.columns[:-1]))


show_test(test_boxplot_cast)


#' <h2>Boxplot with color</h2>


@viz_reg_test
def test_boxplot_color():
    source = data.barley()
    return ar.boxplot(source, columns="yield", group_by="site", color="year:O")


show_test(test_boxplot_color)
