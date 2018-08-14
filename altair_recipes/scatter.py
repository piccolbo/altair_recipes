"""Scatter plots."""
import altair as alt
from .common import default
from .docstrings import make_docstring, Docstring as D


def scatter(data, x, y, mark={}, encoding={}, properties={}):
    """See below."""

    return alt.Chart(data).mark_point(**mark).encode(
        x=x, y=y, **encoding).properties(**properties)


scatter.__doc__ = make_docstring(
    summary="Generate a scatter plot.",
    params=[D.data, D.x, D.y, D.mark, D.encoding, D.properties])


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
    summary="Generate many scatter plots, all vs. all,\
     from several columns(default all)",
    params=[D.data, D.columns, D.group_by, D.mark, D.encoding, D.properties])
