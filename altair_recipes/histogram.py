"""Generate histograms."""
import altair as alt
from .common import multivariate_preprocess
from .docstrings import make_docstring, Docstring as D


def histogram(data, column, mark={}, encoding={}, properties={}):
    """See below."""
    return alt.Chart(data).mark_bar(**mark).encode(
        alt.X(column + ":Q", bin=True), alt.Y("count()"),
        **encoding).properties(**properties)


histogram.__doc__ = make_docstring(
    summary="Generate a histogram.",
    params=[D.column, D.mark, D.encoding, D.properties])


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
    "Generate multiple overlapping histograms.",
    params=[D.columns, D.group_by, D.mark, D.encoding, D.properties])
