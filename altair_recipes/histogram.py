from .common import to_dataframe, gather, UnivariateRecipe, MultivariateRecipe
import altair as alt
from autosig import autosig


@autosig(UnivariateRecipe)
def histogram(data, column, mark={}, encoding={}, properties={}):
    return alt.Chart(data).mark_bar(**mark).encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"),
        **encoding).properties(**properties)


@autosig(MultivariateRecipe)
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
        key = group_by
        value = columns if type(columns) is str else columns[0]
    return alt.Chart(data).mark_area(
        opacity=1 / (len(data[group_by].unique())
                     if group_by is not None else len(columns)),
        interpolate="step",
        **mark).encode(
            alt.X(value + ":Q", bin=True), alt.Y("count()", stack=None),
            alt.Color(key + ":N"), **encoding).properties(**properties)
