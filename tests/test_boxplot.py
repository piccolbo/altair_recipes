import altair_recipes as ar
from altair_recipes.common import viz_reg_test
from altair_recipes.display_altair import show_test
from vega_datasets import data

#' ##  Boxplot from melted data
#+ results='raw'


@viz_reg_test
def test_boxplot_melted():
    return ar.boxplot(data.iris(), columns="petalLength", group_by="species")


show_test(test_boxplot_melted)
#' ##  Boxplot from cast data
#+ results='raw'


@viz_reg_test
def test_boxplot_cast():
    iris = data.iris()
    return ar.boxplot(iris, columns=list(iris.columns[:-1]))


show_test(test_boxplot_cast)
