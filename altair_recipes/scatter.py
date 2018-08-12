from .common import default, BivariateRecipe, MultivariateRecipe
import altair as alt
from autosig import autosig


@autosig(BivariateRecipe)
def scatter(data, x="x", y="y", mark={}, encoding={}, properties={}):
    return alt.Chart(data).mark_point(**mark).encode(
        x=x, y=y, **encoding).properties(**properties)


@autosig(MultivariateRecipe)
def multiscatter(data, columns=None, mark={}, encoding={}, properties={}):
    columns = list(default(columns, data.columns))
    return alt.Chart(data).mark_point(**mark).encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        **encoding).properties(**properties).repeat(
            row=columns, column=columns)
