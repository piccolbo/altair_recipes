import altair as alt
from vega_datasets import data


def scatter(data, x="x", y="y", color=alt.Color(), tooltip=alt.Tooltip()):
    return alt.Chart(data).mark_point().encode(
        x=x, y=y, color=color, tooltip=tooltip)


scatter(
    data.iris(),
    x="petalWidth",
    y='petalLength',
    color="sepalWidth",
    tooltip="species")
