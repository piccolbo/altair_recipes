"""Generate barcharts."""
from .signatures import bivariate_recipe, use_color
import altair as alt
from autosig import autosig, Signature


@autosig(bivariate_recipe + Signature(color=use_color(position=3)))
def barchart(data, x=0, y=1, color=False, height=600, width=800):
    """Generate a barchart."""
    enc_args = dict(x=x + ":N", y=y)
    if color:
        enc_args["color"] = enc_args["x"]

    return alt.Chart(data, height=height, width=width).mark_bar().encode(**enc_args)
