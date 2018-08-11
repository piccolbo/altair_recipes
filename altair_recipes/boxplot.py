"""Boxplot implementation"""
import altair as alt
from altair_recipes.common import default, gather, to_dataframe


#TODO: inject addional option into graph
#TODO: unclear how to do it with complex graphics such as this, if there is a way
def boxplot(data, columns, group_by=None, mark={}, encoding={}, properties={}):
    data = to_dataframe(data)
    assert type(columns) == str or len(columns) == 1 or group_by is None
    # we are doing wide or long format but not both
    if group_by is None:  #convert wide to long
        x = default(data.columns.name, "variable")
        y = "value"
        data = gather(data, key=x, value=y, columns=columns)
    else:
        x = group_by
        y = columns if type(columns) is str else columns[0]
    #long form assumed from here
    chart = alt.Chart(data)
    chart_bar = chart.mark_bar(filled=False)
    chart_tick = chart.mark_tick()
    min_y = "min(" + y + ")"
    max_y = "max(" + y + ")"
    median_y = "median(" + y + ")"
    q1_bar = chart_bar.encode(x=x, y="q1(" + y + ")", y2=median_y)
    q3_bar = chart_bar.encode(x=x, y=median_y, y2="q3(" + y + ")")

    min_tick = chart_tick.encode(x=x, y=min_y)
    max_tick = chart_tick.encode(x=x, y=max_y)
    rule = chart.mark_rule().encode(
        x=x, y=alt.Y(min_y, axis=alt.Axis(title=y)), y2=max_y)
    return q1_bar + q3_bar + min_tick + max_tick + rule
