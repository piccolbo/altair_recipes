from functools import singledispatch
import pandas as pd
import requests



def viz_reg_test(test_f):
    """Decorate recipe tests.

    Transforms a function into a regression test. Also saves chart in html for
    visual inspection in the test directory, named after the file and function
    of the test. If invoked with None as sole argument, the decorated function
    will just produce the chart, disabling the regression machinery, again for
    manual inspection.

    Parameters
    ----------
    test_f : function
        Simple chart-generating argumentless function, pytest-style

    Returns
    -------
    function
        The decorated function.

    """

    def fun(regtest):
        plot = test_f()
        if regtest is not None:
            regtest.write(plot.to_json())
        plot.save(
            test_f.__code__.co_filename + "_" + test_f.__qualname__ + ".html")
        return plot

    return fun


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


def default(*args):
    """Return the first not None of the arguments.

    Parameters
    ----------
    *args : Any
        Any number of arguments.

    Returns
    -------
    Any
        One of the arguments.

    """
    return next(x for x in args if x is not None)


def update_dict(updatee, updates):
    """Update a dict without side effects.

    Parameters
    ----------
    updatee : dict
        The starting point.
    updates : dict
        The updates to apply.

    Returns
    -------
    dict
        A dict with all the key, value pairs in updatee and updates. Whenever a
        key is shared, updates takes precedence.

    """

    u = updatee.copy()
    u.update(updates)
    return u


def update_kwargs(**kwargs):
    updates = kwargs['updates']
    del kwargs['updates']
    return update_dict(kwargs, updates)


def gather(data, key, value, columns):
    """Convert wide format data frame to long format.

    Do so while concatenating selected columns into one and using a new column
    to track their origin.

    Parameters
    ----------
    data : pandas DataFrame
        The data to operate on.
    key : str
        The name of the column tracking the origin of that record.
    value : type
        The name of the column holding all the values previously in a number of
        columns.
    columns : list of str
        The names of the columns to reduce to a single column.

    Returns
    -------
    pandas.DataFrame
        A data frame with a reduced number of columns but the same information.

    """
    return pd.melt(
        data,
        id_vars=[col for col in data.columns if col not in columns],
        value_vars=columns,
        var_name=key,
        value_name=value)


# TODO: this doesn't cover multiscatter which is a multivariate viz but does
# require the data in wide format, this only converts to long (gather)
def multivariate_preprocess(data, columns, group_by):
    """Preprocess data for multivariate graphs.

    Converts to data frame, then turns to long format.

    Parameters
    ----------
    data : pandas.DataFrame
        The data to be processed.
    columns : list of str
        The columns that need to be gathered.
    group_by : str
        The column indicating which vaiable a record refers to (long format).

    Returns
    -------
    (pandas.DataFrame, str, str)
        A tuple with the data in long format, the name of the column indicating
        the variable and the name of of the column holding the values.

    """
    assert type(columns) == str or len(
        columns) == 1 or group_by is None, "Wide or long format but not both"
    if group_by is None:  # convert wide to long
        key = default(data.columns.name, "variable")
        value = "value"
        data = gather(data, key=key, value=value, columns=columns)
    else:
        key = group_by
        value = columns if type(columns) is str else columns[0]
    return data, key, value


def subset_dict(d, keep_keys, exclude_values=[None]):
    return {k: d[k] for k in keep_keys if d[k] not in exclude_values}
