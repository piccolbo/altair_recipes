import altair as alt
from altair_recipes.common import to_dataframe, gather


def histogram(data, column, mark={}, encoding={}, properties={}):
    return alt.Chart(data).mark_bar(**mark).encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"),
        **encoding).properties(**properties)


def layered_histogram(data,
                      columns,
                      group_by=None,
                      mark={},
                      encoding={},
                      properties={}):
    data = to_dataframe(data)
    assert type(columns) == str or len(columns) == 1 or group_by is None
    # we accept wide or long format but not a mix
    if group_by is None:  #convert wide to long
        key = "key"
        value = "value"
        data = gather(data, key=key, value=value, columns=columns)
    else:
    return (alt.Chart(data).mark_area(
        opacity=1 / len(data[color_variable].unique()),
        interpolate="step").encode(
            alt.X(x_label + ":Q", bin=True),
            alt.Y("count()", stack=None),
            alt.Color(color_variable + ":N", scale=color_scale),
        ))
