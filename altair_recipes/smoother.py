"""Smoother graph."""
import altair as alt
from .docstrings import make_docstring


def smoother(data,
             x,
             y,
             window=None,
             interquartile_area=True,
             mark={},
             encoding={},
             properties={}):
    """See below."""
    window = data.shape[0] // 4 if window is None else int(window)
    _data = data.sort_values(by=x)
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


smoother.__doc__ = make_docstring(
    smoother,
    summary="Generate a smooth line plot with optional IRQ shading area",
    additional_params=dict(
        window="""window: int
    The size of the smoothing window""",
        interquartile_area="""interquartile_area: bool
    Whether to plot the IRQ as an area"""))
