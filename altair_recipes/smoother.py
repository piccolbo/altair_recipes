"""Smoother graph."""
from .docstrings import make_docstring
from .signatures import signature, BivariateRecipe
import altair as alt
from autosig import autosig, param


@signature
class Smoother(BivariateRecipe):
    window = param(default=None)
    interquartile_area = param(default=True)


@autosig(Smoother)
def smoother(data, x=0, y=1, window=None, interquartile_area=True):
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
