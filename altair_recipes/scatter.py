"""Scatter plots."""
from .common import default, subset_dict
from .signatures import BivariateRecipe, MultivariateRecipe
import altair as alt
from autosig import autosig, signature, param

color = param(
    default=None,
    docstring="""`str` or `int`
The column containing the data associated with the color of the mark""")

tooltip = param(
    default=None,
    docstring="""`str` or `int`
The column containing the data associated with the tooltip text""")


@signature
class Scatter(BivariateRecipe):
    color = color
    tooltip = tooltip

    def default(self):
        super().default()
        self.to_column("color")
        self.to_column("tooltip")


@autosig(Scatter)
def scatter(data, x=0, y=1, color=None, tooltip=None):
    """Generate a scatter plot."""
    kwargs = subset_dict(locals(), keep_keys=['color', 'tooltip'])
    return alt.Chart(data).mark_point().encode(x=x, y=y, **kwargs)


@signature
class Multiscatter(MultivariateRecipe):
    # TODO: dupicates from line 11 in class Scatter
    color = color
    tooltip = tooltip

    def default(self):
        super().default()
        self.to_column("color")
        self.to_column("tooltip")


@autosig(Multiscatter)
def multiscatter(data, columns=None, group_by=None, color=None, tooltip=None):
    """Generate many scatter plots.

    Based on several columns, pairwise."""
    kwargs = subset_dict(locals(), keep_keys=['color', 'tooltip'])
    columns = list(default(columns, data.columns))
    assert group_by is None, "Long format not supported yet"
    return alt.Chart(data).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'), **kwargs).repeat(
            row=columns, column=columns)
