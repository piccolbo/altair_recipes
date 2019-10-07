"""Converters and other init procedures used to define signatures."""
from attr import attrs, attrib
from functools import singledispatch
from numbers import Number
import pandas as pd
import requests


@singledispatch
def to_dataframe(data):
    """Convert altair.Data to pandas.DataFrame.

    Parameters
    ----------
    data : altair.Data
        The data source to be converted.

    Returns
    -------
    pandas.DataFrame
        A DataFrame with the same data as the `data` argument.

    """
    assert False, "Not implemented:" + str(type(data))


@to_dataframe.register(pd.DataFrame)
def _(data):
    return data


@to_dataframe.register(str)
def _(data):
    return pd.DataFrame(requests.get(data).json())


@to_dataframe.register(type(None))
def _(data):
    return pd.DataFrame()


# argument manip (may belong to signatures)
@attrs
class Column:
    """Class to hold column argument value until late initialization.

    Since certain types of column specification require the knowledge of the column names in the data, the conversion to column name has to be delayed until the data is available. This class holds the data and method to make that possible.

    Parameters
    ----------
    col : int, str, pandas Series or can be converted to it.

    """

    col = attrib()

    def to_str(self, data, name):
        """Convert a col specification to a col name and assign it to a given attribute.

        If it's an int, look at  data positionally to find the col name, otherwise convert to str.

        Parameters
        ----------
        data : any
            DataFrame the Column should come from


        Returns
        -------
        str
            Column name

        """

        value = self.col
        if isinstance(value, (str, type(None))):
            pass
        elif isinstance(value, Number):
            value = data.columns[value]
        else:
            value = pd.Series(value)
            name = value.name or name
            data[name] = value
            value = name

        assert isinstance(value, str) or value is None  # none stands for all columns
        return value


@attrs
class Columns:
    """Class to hold the columns argument value until late initialization.

    See Column for additional explanations.

    Parameters
    ----------
    cols : collection of: int, str, pandas Series or what can be converted to it.

    """

    cols = attrib()

    def to_str(self, data, name):
        """Convert a col set specification to a list of col names.

        It first promotes value to a list if not Iterable, then applies to_column to each element and assigns result to attribute in data. If value is None, it is construed as "all columns in data"

        Parameters
        ----------
        data : any
            DataFrame the Columns should come from.


        Returns
        -------
        list of str
            List of column names

        """

        value = self.cols
        value = (
            list(data.columns)
            if value is None
            else (
                [
                    Column(c).to_str(data, "c" + str(i))
                    for c, i in zip(value, range(len(value)))
                ]
            )
        )

        for v in value:
            assert isinstance(v, str) or v is None
        return value


def init_cols(param_dict):
    """Perform late initialization of columns.

    Since both data and columns of different types are needed to complete initialization, this is done during late initialization with this function. Acts by side effects on param_dict.

    """
    for name, arg in param_dict.items():
        if isinstance(arg, (Column, Columns)):
            param_dict[name] = param_dict[name].to_str(param_dict["data"], name)
