"""Generate barcharts."""
from .signatures import bivariate_recipe, color
import altair as alt
from autosig import autosig, Signature


@autosig(bivariate_recipe + Signature(color=color(default=None, position=3)))
def barchart(data, x=0, y=1, color=None, height=600, width=800):
    """Generate a barchart."""
    enc_args = dict(x=x, y=y)
    if color is not None:
        enc_args["color"] = color

    return alt.Chart(data, height=height, width=width).mark_bar().encode(**enc_args)
