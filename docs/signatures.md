

| fname             | data | channel      | channel       | channel    | channel      | channel      | stats               | stats                   | size       | size      |
| ----------------- | ---- | ------------ | ------------- | ---------- | ------------ | ------------ | ------------------- | ----------------------- | ---------- | --------- |
| autocorrelation   | data | column=0     |               |            |              |              | max_lag=None        |                         | height=600 | width=800 |
| autoplot          | data | columns=None | group_by=None |            |              |              |                     |                         | height=600 | width=800 |
| barchart          | data | x=0          | y=1           |            |              |              |                     |                         | height=600 | width=800 |
| boxplot           | data | columns=None | group_by=None | color=None |              |              |                     |                         | height=600 | width=800 |
| heatmap           | data | x=0          | y=1           | color=2    | opacity=None |              | aggregate='average' |                         | height=600 | width=800 |
| histogram         | data | column=0     |               |            |              |              |                     |                         | height=600 | width=800 |
| layered_histogram | data | columns=None | group_by=None |            |              |              |                     |                         | height=600 | width=800 |
| multiscatterplot  | data | columns=None | group_by=None | color=None | opacity=1    | tooltip=None |                     |                         | height=600 | width=800 |
| qqplot            | data | x=0          | y=1           |            |              |              |                     |                         | height=600 | width=800 |
| scatterplot       | data | x=0          | y=1           | color=None | opacity=1    | tooltip=None |                     |                         | height=600 | width=800 |
| smoother          | data | x=0          | y=1           |            |              |              | window=None         | interquartile_area=True | height=600 | width=800 |
| stripplot         | data | columns=None | group_by=None | color=None | opacity=1    |              |                     |                         | height=600 | width=800 |


Split parameters into 4 groups, data, channel, stats  and view. Data is the same for all, a dataframe or equivalent. View should be the same for all and have properties such as height, width and bg color.
channel, which is actually like encoding, varies the most for different chart types. There is the uni-, bi- or multi-variate variety, then there are the optional color, opacity and tooltip. Then there are the more statistical params also variable from case to case.


Classes for groups of arguments

someplot(data, Channels(x = "x", y="y"), Stats(window = 10), View(height=50))

But for instance Channels should also accept column or columns instead. So we are going ot have an __init__ with lots of params and less visibility for the user. If we have a specific class for someplot, then this could look like


barchart(data, ChannelsBar(x="x", y="y"), StatsBar(), View(height=50))

which solves the problem of the ever growing number of params and provide more help to the user. One would type help barchart and find that it takes a BarChannel and BarStats and then do help(BarChannel) and learn about x and y. Passing the wrong params would fail instantly with the correct error message. But the proliferation of classes is remarkable an the names are silly. The classes wouldn't require any more code than autosig does for function and would be implemented concisely with attr.


Methods, like altair

barchart(data).encode(x="x", y="y").stats(max_lag=None).view(height=50)

micromethods

barchart.data(data).x("x").y("y").max_lag(None).view(height=50)

Partial currying

barchart(data)(x="x", y="y")(max_lag=None)(height=50)

Each function return a callable which takes the next set of parameters. One avoids the too many params trap. Documentation for barchart gets scattered over many functions. Order is important but IDE should help. When all values at default one may end with something silly like barchart(data)()()() instead of barchart(data)
