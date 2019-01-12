"""Generate barcharts."""
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature


@autosig(bivariate_recipe + Signature(color=color(default=None, position=3)))
def barchart(data, x=0, y=1, color=None, height=300, width=400):
    """Generate a barchart."""
    chart = alt.Chart(
        data,
        height=height,
        width=width / ((len(data[x].unique()) if color is not None else 1)),
    ).mark_bar()
    if color is None:
        return chart.encode(x=x, y=y)
    else:
        return chart.encode(x=alt.X(color, axis=None), y=y, color=color, column=x)
