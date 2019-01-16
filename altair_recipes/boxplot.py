"""Boxplot implementation."""
from .common import multivariate_preprocess, ndistinct
from .signatures import multivariate_recipe, color
import altair as alt
from autosig import autosig, Signature


@autosig(multivariate_recipe + Signature(color=color(default=None, position=3)))
def boxplot(data, columns=None, group_by=None, color=None, height=600, width=800):
    """Generate a boxplot."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    # long form assumed from here
    chart = alt.Chart(
        height=height, width=width / ndistinct(data, key, color is not None)
    )
    chart_bar = chart.mark_bar(stroke="black", fill="#4682b4")
    chart_tick = chart.mark_tick()
    encode_args = dict(x=key) if color is None else dict(x=alt.X(color, axis=None))
    min_value = "min(" + value + ")"
    max_value = "max(" + value + ")"
    median_value = "median(" + value + ")"
    min_tick = chart_tick.encode(y=min_value, **encode_args)
    max_tick = chart_tick.encode(y=max_value, **encode_args)
    q1 = "q1(" + value + ")"
    q3 = "q3(" + value + ")"
    if color is not None:
        encode_args["color"] = color
    q1_bar = chart_bar.encode(y=q1, y2=median_value, **encode_args)
    q3_bar = chart_bar.encode(y=median_value, y2=q3, **encode_args)

    rule = chart.mark_rule().encode(
        y=alt.Y(min_value, axis=alt.Axis(title=value)), y2=max_value, **encode_args
    )
    bplot = rule + min_tick + max_tick + q1_bar + q3_bar
    return (
        bplot.properties(data=data)
        if color is None
        else bplot.facet(data=data, column=key)
    )
