"""Generate barcharts."""
from .signatures import bivariate_recipe, column
import altair as alt
from autosig import autosig, Signature


@autosig(
    bivariate_recipe
    + Signature(
        column=column(
            default=None,
            position=3,
            docstring="The column containing the data associated with horizontal faceting",
        ),
        row=column(
            default=None,
            position=4,
            docstring="The column containing the data associated with vertical faceting",
        ),
    )
)
def barchart(data, x=0, y=1, column=None, row=None, height=600, width=800):
    """Generate a barchart."""
    enc_args = dict(x=x, y=y)
    if column is not None:
        enc_args["x"] = alt.X(x, axis=None)
        enc_args["color"] = x
        enc_args["column"] = column
    if row is not None:
        enc_args["row"] = row

    return (
        alt.Chart(
            data,
            height=height / (len(data[row].unique()) if row is not None else 1),
            width=width / (len(data[column].unique()) if column is not None else 1),
        )
        .mark_bar()
        .encode(**enc_args)
    )
