"""Reusable docstrings elements."""
from enum import Enum


class Docstring(Enum):
    """Reusable docstring elements collected in an enum."""

    data = """data: Altair Data or pandas DataFrame or csv or json file URL
    The data from which the statistical graphics is being generated"""
    column = """column: str or other column selector
    The column containing the data to be used in the graphics"""
    x = """x: str or other columns selector
    The column containing the data associated with the horizontal dimension"""
    y = """y: str or other column selector
    The column containing the data associated with the vertical dimension"""
    columns = """columns: str or list thereof or other column selector
    The column or columns to be used in the graphics"""
    group_by = """group_by: str or other column selector
    The column to be used to group the data when in long form. When group_by is
    specified columns should point to a single column"""
    return_object = """altair.Chart_area
    The graphics object"""
    mark = """mark: dictionary
    Additional arguments to pass to the mark method of Chart"""
    encoding = """encoding: dictionary
    Additional arguments to the encode method of Chart"""
    properties = """properties: dictionary
    Additional arguments to the properties method of Chart"""
    returns = """altair.Chart
    The chart described in the summary"""


def make_docstring(summary, params, returns=Docstring.returns):
    """Make docstrings from simple reusable parts.

    Parameters
    ----------
    summary : str
        The docstring summary.
    params : str
        A list of parameter docstrings. If present in the .docstrings.Docstring
        enum, will be replaced by corresponding value (default meaning for that
        argument)
    returns : str
        The docstring return section. If just "returns", will be replaced by
        .docstrings.Docstring.returns

    Returns
    -------
    str
        A docstring. Assign to __doc__ of desired object.

    """
    params = list(
        map(lambda x: x.value if type(x) == Docstring else x, params))
    returns = returns.value if type(returns) == Docstring else returns
    return "    \n".join([summary, "\nParameters\n---------"] + params +
                         ["\nReturns\n-------", returns])
