"""Mini-library for all the other modules."""
import altair as alt
from boltons.iterutils import remap
from logging import warning
import numpy as np
import pandas as pd
import pytest_regtest
from toolz.dicttoolz import keyfilter, valfilter


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


# testing
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
        with alt.data_transformers.enable(consolidate_datasets=False):
            np.random.seed(seed=0)
            plot = test_f()
            if regtest is not None:
                regtest.write(
                    alt.Chart.from_dict(round_floats(plot.to_dict(), 13)).to_json()
                )
                plot.save(
                    test_f.__code__.co_filename + "_" + test_f.__qualname__ + ".html"
                )
            return plot

    test_f.__doc__ = (
        (
            test_f.__doc__
            or "Test for function {test_f}".format(test_f=test_f.__qualname__)
        )
        + """
    Parameters
    ----------
    Pass a single unnamed argument equal None to manually  execute outside regression testing. In that case it returns a chart.
    """
    )
    return fun


@pytest_regtest.register_converter_pre
def fix_before(txt):
    """Remove schema information from regression data."""

    # remove lines with passwords:
    lines = txt.split('\n')
    lines = [l for l in lines if "https://vega.github.io/schema/vega-lite/" not in l]
    return '\n'.join(lines)

# collections


def check_distinct(data, col, group=None):
    """Check that a column of data contains unique values, optionally within each group defined by group.

    Parameters
    ----------
    data : dataframe
        The data.
    col : int or str or other pandas col
        The column of data to check.
    group : mapping, function, label, or list of labels
        optionally group by this and check uniqueness within each group (the default is None or do not group). See pandas.DataFrame.groupby for details.

    Returns
    -------
    bool
        True if all element distinct, for all groups within each group if group is not None.

    """
    if group is None:
        x = data[col]
        return x.size == x.nunique()
    else:
        x = data.groupby(group)[col]
        return all(x.size() == x.nunique())

def warn_not_distinct(data, col, group=None):
    """Generate warning if not distinct, see check_distinct."""

    if not check_distinct(data, col, group):
        warning("The relation to plot is not a function")


def choose_kwargs(from_, which):
    """Choose entries for a dictionary with key in `which` and not None value."""
    return keyfilter(lambda x: x in which, valfilter(lambda x: x is not None, from_))


def round_floats(a_dict, precision):
    """Find all the floats in `a_dict` (recursive) and round them to `precision`."""
    return remap(
        a_dict,
        lambda p, k, v: (k, round(v, precision)) if isinstance(v, float) else (k, v),
    )


def ndistinct(data, column):
    """Return number of distinct elements in data[column]."""
    return len(data[column].unique())


def col_cardinality(data, column, condition=None, default=1):
    """Return number of distinct elements in `data[column]` if `condition` is True (defaults to `column` being different from None), otherwise return `default`."""
    if condition is None:
        condition = column is not None
    return ndistinct(data, column) if condition else default


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
        value_name=value,
    )


# TODO: this doesn't cover multiscatterplot which is a multivariate viz but does
# require the data in wide format, this only converts to long (gather)
# To include multiscatterplot one would need an index column or set thereof


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
    assert (
        type(columns) == str or len(columns) == 1 or group_by is None
    ), "Wide or long format but not both"
    if group_by is None:  # convert wide to long
        key = default(data.columns.name, "variable")
        value = "value"
        data = gather(data, key=key, value=value, columns=columns)
    else:
        key = group_by
        value = columns if type(columns) is str else columns[0]
    return data, key, value


# constant luminosity and chroma scales

hue_scale_light = alt.Scale(type="linear", range=["#F271B8", "#00B4D7"])
hue_scale_dark = alt.Scale(type="linear", range=["#C10083", "#0080A7"])

# chart combinators


def layer(*layers, **kwargs):
    """Layer charts: a drop in replacement for altair.layer that does a deepcopy of the layers to avoid side-effects and lifts identical datasets one level down to top level."""
    layers = [l.copy() for l in layers]
    data = layers[0].data
    if all(map(lambda l: data.equals(l.data), layers)):
        layered = alt.layer(*layers, **kwargs, data=data)
        for l in layered.layer:
            del l._kwds["data"]
    else:
        layered = alt.layer(*layers, **kwargs)

    return layered
