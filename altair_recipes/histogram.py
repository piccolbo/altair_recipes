"""Generate histograms."""
from .common import multivariate_preprocess
from .docstrings import make_docstring
from .signatures import UnivariateRecipe, MultivariateRecipe
import altair as alt
from autosig import autosig


@autosig(UnivariateRecipe)
def histogram(
        data,
        column=0,
):
    """See below."""
    return alt.Chart(data).mark_bar().encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"))


histogram.__doc__ = make_docstring(histogram, summary="Generate a histogram")


@autosig(MultivariateRecipe)
def layered_histogram(
        data,
        columns=None,
        group_by=None,
):
    """See below."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    return alt.Chart(data).mark_area(
        opacity=1 / (len(data[group_by].unique())
                     if group_by is not None else len(columns)),
        interpolate="step",
    ).encode(
        alt.X(value + ":Q", bin=True), alt.Y("count()", stack=None),
        alt.Color(key + ":N"))


layered_histogram.__doc__ = make_docstring(
    layered_histogram, "Generate multiple overlapping histograms")
