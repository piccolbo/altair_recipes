"""Boxplot implementation."""
from .common import multivariate_preprocess
from .signatures import multivariate_recipe, use_color
import altair as alt
from autosig import autosig, Signature


@autosig(multivariate_recipe + Signature(color=use_color(position=3)))
def boxplot(data=None, columns=None, group_by=None, color=False, height=600, width=800):
    """Generate a boxplot."""
    data, key, value = multivariate_preprocess(data, columns, group_by)
    # long form assumed from here
    chart = alt.Chart(height=height, width=width)
    chart_bar = chart.mark_bar(stroke="black", fill="#4682b4")

    chart_tick = chart.mark_tick(color="black")
    x = key + ":N"
    stats = {
        stat: stat + "(" + value + ")" for stat in ["min", "max", "median", "q1", "q3"]
    }
    ticks = {tick: chart_tick.encode(x=x, y=stats[tick]) for tick in ["min", "max"]}
    encode_args = dict(x=x)
    if color:
        encode_args["fill"] = key + ":N"
    q1_bar = chart_bar.encode(y=stats["q1"], y2=stats["median"], **encode_args)
    q3_bar = chart_bar.encode(y=stats["median"], y2=stats["q3"], **encode_args)

    rule = chart.mark_rule().encode(
        x=x, y=alt.Y(stats["min"], axis=alt.Axis(title=value)), y2=stats["max"]
    )
    return (rule + ticks["min"] + ticks["max"] + q1_bar + q3_bar).properties(data=data)
