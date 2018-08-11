import altair as alt
from altair_recipes.common import to_dataframe, gather


def histogram(data, column, mark={}, encoding={}, properties={}):
    return alt.Chart(data).mark_bar(**mark).encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"),
        **encoding).properties(**properties)


def layered_histogram(data,
    if len(count_variables) == 1:
        x_label = count_variables[0] if x_label is None else str(x_label)
        assert color_variable is not None
                      columns,
                      group_by=None,
                      mark={},
                      encoding={},
                      properties={}):
    data = to_dataframe(data)
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
