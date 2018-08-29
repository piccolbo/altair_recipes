"""Reusable docstrings elements."""
from inspect import signature

docstrings = dict(
    data="""data: `altair.Data` or `pandas.DataFrame` or csv or json file URL
    The data from which the statistical graphics is being generated""",
    column="""column: `str` or `int`
    The column containing the data to be used in the graphics""",
    x="""x: `str` or `int`
    The column containing the data associated with the horizontal dimension""",
    y="""y: `str` or `int`
    The column containing the data associated with the vertical dimension""",
    columns="""columns: `str` or `int` or `list` thereof
    The column or columns to be used in the graphics""",
    group_by="""group_by: `str` or `int`
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column""",
    color="""color: `str` or `int`
    The column containing the data associated with the color of the mark""",
    tooltip="""tooltip: `str` or `int`
    The column containing the data associated with the tooltip text""",
    returns="""`altair.Chart`
    The chart described in the summary""")


def make_docstring(func, summary, additional_params={}):
    """Make docstrings from simple reusable parts.

    Parameters
    ----------
    summary : str
        The docstring summary.
    additional_params : dict
        A list of parameter docstrings. If present in the .docstrings.Docstring
        enum, will be replaced by corresponding value (default meaning for that
        argument)


    Returns
    -------
    str
        A docstring. Assign to __doc__ of desired object.

    """
    docstrings_ = docstrings.copy()
    docstrings_.update(additional_params)
    params = list(
        map(lambda x: docstrings_[x],
            signature(func).parameters.keys()))
    returns = docstrings['returns']
    return "\n".join([summary + ".", "\nParameters\n---------"] + [
        ".\n".join(params),
        "\nReturns\n-------",
        returns,
    ]) + "."
