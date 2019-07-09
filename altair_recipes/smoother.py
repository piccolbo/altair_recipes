"""Smoother graph."""
from .signatures import bivariate_recipe
import altair as alt
from autosig import autosig, param, Signature


@autosig(
    bivariate_recipe
    + Signature(
        window=param(
            default=None,
            position=3,
            docstring="""int
    The size of the smoothing window""",
        ),
        interquartile_area=param(
            default=True,
            position=4,
            docstring="""interquartile_area: bool
    Whether to plot the IRQ as an area""",
        ),
    )
)
def smoother(
    data, x=0, y=1, window=None, interquartile_area=True, height=600, width=800
):
    """Generate a smooth line plot with optional IRQ shading area."""
    window = data.shape[0] // 4 if window is None else int(window)
    _data = data.sort_values(by=x)
    _data[x] = _data[x].rolling(window).median()
    _data["median"] = _data[y].rolling(window).median()
    chart_line = (
        alt.Chart(height=height, width=width).mark_line().encode(x=x, y="median")
    )
    if interquartile_area:
        _data["q1"] = _data[y].rolling(window).quantile(0.25)
        _data["q3"] = _data[y].rolling(window).quantile(0.75)
        chart_area = (
            alt.Chart(height=height, width=width)
            .mark_area(opacity=0.2)
            .encode(x=x, y=alt.Y("q1", title=y), y2="q3")
        )
        chart = chart_line + chart_area
    else:
        chart = chart_line
    return chart.properties(data=_data)
