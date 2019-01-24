"""Generate histograms."""
from .common import multivariate_preprocess, col_cardinality
from .signatures import univariate_recipe, multivariate_recipe
import altair as alt
from autosig import autosig


@autosig(univariate_recipe)
def histogram(data, column=0, height=600, width=800):
    """Generate a histogram."""
    return (
        alt.Chart(data, height=height, width=width)
        .mark_bar()
        .encode(alt.X(column, bin=True), alt.Y("count()"))
    )


@autosig(multivariate_recipe)
def layered_histogram(data, columns=None, group_by=None, height=600, width=800):
    """Generate multiple overlapping histograms."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    return (
        alt.Chart(data, height=height, width=width)
        .mark_area(
            opacity=1 / col_cardinality(data, group_by, default=len(columns)),
            interpolate="step",
        )
        .encode(alt.X(value, bin=True), alt.Y("count()", stack=None), alt.Color(key))
    )
