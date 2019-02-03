"""Generate stripplots."""
from .common import multivariate_preprocess
from .signatures import multivariate_recipe, opacity, color
import altair as alt
from autosig import autosig, Signature


@autosig(
    multivariate_recipe
    + Signature(color=color(default=None, position=3), opacity=opacity(position=4))
)
def stripplot(
    data, columns=None, group_by=None, color=None, opacity=1, height=600, width=800
):
    """Generate a stripplot."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    enc_args = dict()
    if color is not None:
        enc_args["color"] = color
    return (
        alt.Chart(data, height=height, width=width)
        .mark_tick(opacity=opacity, thickness=2)
        .encode(x=key + ":N", y=value, **enc_args)
    )
