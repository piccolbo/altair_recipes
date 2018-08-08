import altair as alt
from vega_datasets import data


def scatter(data, x="x", y="y", color=alt.Color(), tooltip=alt.Tooltip()):
    return alt.Chart(data).mark_point().encode(
        x=x, y=y, color=color, tooltip=tooltip)


def multiscatter(data,
                 variables=None,
                 color=alt.Color(),
                 tooltip=alt.Tooltip(),
                 width=None,
                 height=None):
    variables = list(data.columns) if variables is None else list(variables)
    ncol = data.shape[1]
    width = 1600 // ncol if width is not None else int(width)
    height = width is height is None else int(height) 
    return alt.Chart(data).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color=color).properties(
            width=width, height=height).repeat(
                row=variables, column=variables)


scatter(
    data.iris(),
    x="petalWidth",
    y='petalLength',
    color="sepalWidth",
    tooltip="species")

multiscatter(data.iris())

multiscatter(data.iris(), variables=data.iris().columns[:-1], color="species")

data.iris().columns[:-1]
