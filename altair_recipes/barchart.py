"""Generate barcharts."""
from .common import ndistinct
from .signatures import bivariate_recipe, column
import altair as alt
from autosig import autosig, Signature


@autosig(
    bivariate_recipe
    + Signature(
        hfacet=column(
            default=None,
            position=3,
            docstring="The column containing the data associated with horizontal faceting",
        ),
        vfacet=column(
            default=None,
            position=4,
            docstring="The column containing the data associated with vertical faceting",
        ),
    )
)
def barchart(data, x=0, y=1, hfacet=None, vfacet=None, height=600, width=800):
    """Generate a barchart, optionally faceted."""
    enc_args = dict(x=x, y=y)
    if hfacet is not None:
        enc_args["x"] = alt.X(x, axis=None)
        enc_args["color"] = x
        enc_args["column"] = hfacet
    if vfacet is not None:
        enc_args["row"] = vfacet

    return (
        alt.Chart(
            data,
            height=height / ndistinct(data, vfacet),
            width=width / ndistinct(data, hfacet),
        )
        .mark_bar()
        .encode(**enc_args)
    )
