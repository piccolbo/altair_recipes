"""Scatter plots."""
import altair as alt
from autosig import autosig, signature, param
from .common import default, BivariateRecipe, MultivariateRecipe, subset_dict
from .docstrings import make_docstring


@signature
class Scatter(BivariateRecipe):
    color = param(default=None)
    tooltip = param(default=None)


@autosig(Scatter)
def scatter(data, x, y, color=None, tooltip=None):
    """See below."""
    kwargs = subset_dict(locals(), keep_keys=['color', 'tooltip'])
    return alt.Chart(data).mark_point().encode(x=x, y=y, **kwargs)


scatter.__doc__ = make_docstring(scatter, summary="Generate a scatter plot")


@signature
class Multiscatter(MultivariateRecipe):
    color = param(default=None)
    tooltip = param(default=None)


@autosig(Multiscatter)
def multiscatter(data, columns=None, group_by=None, color=None, tooltip=None):
    """See below."""
    kwargs = subset_dict(locals(), keep_keys=['color', 'tooltip'])
    columns = list(default(columns, data.columns))
    assert group_by is None, "Long format not supported yet"
    return alt.Chart(data).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'), **kwargs).repeat(
            row=columns, column=columns)


multiscatter.__doc__ = make_docstring(
    multiscatter,
    summary="Generate many scatter plots, all vs. all,\
     from several columns(default all)")
