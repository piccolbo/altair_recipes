import altair as alt


def scatter(data, x="x", y="y", color=alt.Color(), tooltip=alt.Tooltip()):
    return alt.Chart(data).mark_point().encode(
        x=x, y=y, color=color, tooltip=tooltip)


def multiscatter(data,
                 variables=None,
                 color=alt.Color(),
                 tooltip=alt.Tooltip(),
                 width=None,
                 height=None):
    variables = list(data.columns) if variables is None else list(variables)
    ncol = data.shape[1]
    width = 1600 // ncol if width is None else int(width)
    height = width if height is None else int(height)
    return alt.Chart(data).mark_point().encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color=color).properties(
            width=width, height=height).repeat(
                row=variables, column=variables)
