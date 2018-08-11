import altair as alt


def scatter(data, x="x", y="y", mark={}, encoding={}, properties={}):
    return alt.Chart(data).mark_point(**mark).encode(
        x=x, y=y, **encoding).properties(**properties)


    variables = list(data.columns) if variables is None else list(variables)
    ncol = data.shape[1]
    width = 1600 // ncol if width is None else int(width)
    height = width if height is None else int(height)
    return alt.Chart(data).mark_point().encode(
def multiscatter(data, variables=None, mark={}, encoding={}, properties={}):
    variables = list(default(variables, data.columns))
    return alt.Chart(data).mark_point(**mark).encode(
        alt.X(alt.repeat("column"), type='quantitative'),
        alt.Y(alt.repeat("row"), type='quantitative'),
        color=color).properties(
            width=width, height=height).repeat(
                row=variables, column=variables)
