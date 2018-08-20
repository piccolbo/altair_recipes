"""Generate histograms."""
import altair as alt
from autosig import autosig
from .common import (multivariate_preprocess, UnivariateRecipe,
                     MultivariateRecipe)
from .docstrings import make_docstring


@autosig(UnivariateRecipe)
def histogram(data, column, mark={}, encoding={}, properties={}):
    """See below."""
    return alt.Chart(data).mark_bar(**mark).encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"),
        **encoding).properties(**properties)


histogram.__doc__ = make_docstring(histogram, summary="Generate a histogram")


@autosig(MultivariateRecipe)
def layered_histogram(data,
                      columns=None,
                      group_by=None,
                      mark={},
                      encoding={},
                      properties={}):
    """See below."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    return alt.Chart(data).mark_area(
        opacity=1 / (len(data[group_by].unique())
                     if group_by is not None else len(columns)),
        interpolate="step",
        **mark).encode(
            alt.X(value + ":Q", bin=True), alt.Y("count()", stack=None),
            alt.Color(key + ":N"), **encoding).properties(**properties)


layered_histogram.__doc__ = make_docstring(
    layered_histogram, "Generate multiple overlapping histograms")
