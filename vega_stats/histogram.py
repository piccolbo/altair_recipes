import altair as alt
from vega_datasets import data
import pandas as pd
import numpy as np


def histogram(data, variable):
    return (alt.Chart(data).mark_bar().encode(
        alt.X(variable + ":Q", bin=True), alt.Y("count()")))


def layered_histogram(data,
                      count_variables,
                      color_variable=None,
                      color_scale=alt.Scale(),
                      x_label=None,
                      y_label=None):
    if len(count_variables) == 1:
        x_label = count_variables[0] if x_label is None else str(x_label)
        assert color_variable is not None
    else:
        x_label = "Value" if x_label is None else str(x_label)
        color_variable = "__color__"
        data = pd.melt(
            data,
            id_vars=data.index.name,
            value_vars=count_variables,
            var_name=color_variable,
            value_name=x_label)
    return (alt.Chart(data).mark_area(
        opacity=1 / len(data[color_variable].unique()),
        interpolate="step").encode(
            alt.X(x_label + ":Q", bin=True),
            alt.Y("count()", stack=None),
            alt.Color(color_variable + ":N", scale=color_scale),
        ))


source = data.movies()

histogram(source, "IMDB_Rating")

df = pd.DataFrame({
    'Trial A': np.random.normal(0, 0.8, 1000),
    'Trial B': np.random.normal(-2, 1, 1000),
    'Trial C': np.random.normal(3, 2, 1000)
})

layered_histogram(df, ["Trial A", "Trial B", "Trial C"])
