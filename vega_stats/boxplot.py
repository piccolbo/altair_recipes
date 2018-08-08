import altair as alt
import pandas as pd
from vega_datasets import data


def boxplot(data, x="x", y="y"):
    if type(x) is not str:
        cols = x
        x = x.name or "variables"
        data = pd.melt(
            data,
            id_vars=data.index.name,
            value_vars=cols,
            var_name=x,
            value_name=y)
    chart = alt.Chart(data)
    chart_bar = chart.mark_bar(filled=False)
    chart_tick = chart.mark_tick()
    min_y = "min(" + y + ")"
    max_y = "max(" + y + ")"
    median_y = "median(" + y + ")"
    q1_bar = chart_bar.encode(x=x, y="q1(" + y + "):Q", y2=median_y)
    q3_bar = chart_bar.encode(x=x, y=median_y, y2="q3(" + y + "):Q")

    min_tick = chart_tick.encode(x=x, y=min_y)
    max_tick = chart_tick.encode(x=x, y=max_y)
    rule = chart.mark_rule().encode(
        x=x, y=alt.Y(min_y, axis=alt.Axis(title=y)), y2=max_y)
    return q1_bar + q3_bar + min_tick + max_tick + rule


iris = data.iris()
boxplot(iris, "species", "petalLength")
iris.columns.name = "vars"

boxplot(iris, pd.Series(["petalLength", "sepalLength"], name="lengths"),
        "length")
