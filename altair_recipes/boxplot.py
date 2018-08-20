"""Boxplot implementation."""
import altair as alt
from autosig import autosig
from .common import (multivariate_preprocess, update_kwargs as uk,
                     MultivariateRecipe)
from .docstrings import make_docstring


@autosig(MultivariateRecipe)
def boxplot(data,
            columns=None,
            group_by=None,
            mark={},
            encoding={},
            properties={}):
    """See below."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    #long form assumed from here
    chart = alt.Chart(data)
    chart_bar = chart.mark_bar(**uk(filled=False, updates=mark))
    chart_tick = chart.mark_tick(**mark)
    min_value = "min(" + value + ")"
    max_value = "max(" + value + ")"
    median_value = "median(" + value + ")"
    q1_bar = chart_bar.encode(
        **uk(x=key, y="q1(" + value + ")", y2=median_value, updates=encoding))
    q3_bar = chart_bar.encode(
        **uk(x=key, y=median_value, y2="q3(" + value + ")", updates=encoding))

    min_tick = chart_tick.encode(**uk(x=key, y=min_value, updates=encoding))
    max_tick = chart_tick.encode(**uk(x=key, y=max_value, updates=encoding))
    rule = chart.mark_rule(**mark).encode(**uk(
        x=key,
        y=alt.Y(min_value, axis=alt.Axis(title=value)),
        y2=max_value,
        updates=encoding))
    return (
        q1_bar + q3_bar + min_tick + max_tick + rule).properties(**properties)


boxplot.__doc__ = make_docstring(
    boxplot,
    summary="""Generate a boxplot.

The additional arguments mark and encoding affect all the marks and
encodings (all the elements of a boxplot)""")
