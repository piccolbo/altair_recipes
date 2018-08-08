import altair as alt
import supersmoother as supsmu
import pandas as pd
import numpy as np


def smoother(data, x="x", y="y", window=None, interquartile_area=True):
    window = data.shape[0] // 4 if window is None else int(window)
    _data = data.sort_values(by="x")
    _data["x"] = _data["x"].rolling(window).median()
    _data["median"] = _data["y"].rolling(window).median()
    chart_line = alt.Chart(_data).mark_line().encode(x=x, y="median")
    if interquartile_area:
        _data["q1"] = _data["y"].rolling(window).quantile(.25)
        _data["q3"] = _data["y"].rolling(window).quantile(.75)
        chart_area = alt.Chart(_data).mark_area(opacity=.2).encode(
            x=x, y="q1", y2="q3")
        return chart_line + chart_area
    else:
        return chart_line


x = np.random.uniform(size=100)
data = pd.DataFrame(dict(x=x, y=np.random.uniform(size=100) + 10 * x))

smoother(data) + alt.Chart(data).mark_point().encode(x="x", y="y")
