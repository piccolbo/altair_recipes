"""Generate histograms."""
from .common import multivariate_preprocess
from .signatures import univariate_recipe, multivariate_recipe
import altair as alt
from autosig import autosig


@autosig(univariate_recipe)
def histogram(data, column=0, height=300, width=400):
    """Generate a histogram."""
    return (
        alt.Chart(data, height=height, width=width)
        .mark_bar()
        .encode(alt.X(column + ":Q", bin=True), alt.Y("count()"))
    )


@autosig(multivariate_recipe)
def layered_histogram(data, columns=None, group_by=None, height=300, width=400):
    """Generate multiple overlapping histograms."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    return (
        alt.Chart(data, height=height, width=width)
        .mark_area(
            opacity=1
            / (len(data[group_by].unique()) if group_by is not None else len(columns)),
            interpolate="step",
        )
        .encode(
            alt.X(value + ":Q", bin=True),
            alt.Y("count()", stack=None),
            alt.Color(key + ":N"),
        )
    )
