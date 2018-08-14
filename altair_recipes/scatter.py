"""Scatter plots."""
import altair as alt
from .common import default
from .docstrings import make_docstring


def scatter(data, x, y, mark={}, encoding={}, properties={}):
    """See below."""

    return alt.Chart(data).mark_point(**mark).encode(
        x=x, y=y, **encoding).properties(**properties)


scatter.__doc__ = make_docstring(scatter, summary="Generate a scatter plot")


def multiscatter(data,
                 columns=None,
                 group_by=None,
                 mark={},
                 encoding={},
                 properties={}):
    """See below."""

    columns = list(default(columns, data.columns))
    assert group_by is None, "Long format not supported yet"
    return alt.Chart(data).mark_point(**mark).encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        **encoding).properties(**properties).repeat(
            row=columns, column=columns)


multiscatter.__doc__ = make_docstring(
    multiscatter,
    summary="Generate many scatter plots, all vs. all,\
     from several columns(default all)")
