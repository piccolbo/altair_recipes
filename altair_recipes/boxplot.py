"""Boxplot implementation."""
from .common import multivariate_preprocess
from .docstrings import make_docstring
from .signatures import MultivariateRecipe
import altair as alt
from autosig import autosig


@autosig(MultivariateRecipe)
def boxplot(
        data,
        columns=None,
        group_by=None,
):
    """See below."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    #long form assumed from here
    chart = alt.Chart(data)
    chart_bar = chart.mark_bar(filled=False)
    chart_tick = chart.mark_tick()
    min_value = "min(" + value + ")"
    max_value = "max(" + value + ")"
    median_value = "median(" + value + ")"
    q1_bar = chart_bar.encode(x=key, y="q1(" + value + ")", y2=median_value)
    q3_bar = chart_bar.encode(x=key, y=median_value, y2="q3(" + value + ")")

    min_tick = chart_tick.encode(x=key, y=min_value)
    max_tick = chart_tick.encode(x=key, y=max_value)
    rule = chart.mark_rule().encode(
        x=key, y=alt.Y(min_value, axis=alt.Axis(title=value)), y2=max_value)
    return (q1_bar + q3_bar + min_tick + max_tick + rule)


boxplot.__doc__ = make_docstring(boxplot, summary="Generate a boxplot")
