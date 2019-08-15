---
layout: post
title: "altair_recipes: a Python package to generate essential statistical graphics for the web"
date: "2019-02-14 17:32:04 -0800"
---

If you don't need the full power of the *grammar of graphics* to generate classical plots for the web `altair_recipes` is the the easy way. Check it out with `pip install altair_recipes`.

<!-- more -->

## Preliminaries

`vega` is a statistical graphics system for the web, meaning charts are displayed in a browser. As an added bonus, it supports interactions, again through web technologies: select data point, reveal information on hover etc. Interactive graphics for the web are the future of statistical graphics. Even the successor to the famous `ggplot` for R, `ggvis`, is based on `vega` (I am glossing over the distinction between `vega` and `vega-lite` here for brevity).

`altair` is a python package that produces `vega` graphics. Like `vega`, it adopts an approach to describing statistical graphics known as *grammar of graphics*   which underlies other well known packages such as `ggplot` for R. It represents an extremely useful compromise of power and flexibility. Its elements are data, marks (points, lines), encodings (relations between data and marks), scales etc.

## Why `altair_recipes`?

Sometimes we want to skip all of that and just produce a *boxplot* (or *heatmap* or *histogram*) in the simplest possible way:


```python
from  altair_recipes import boxplot
from altair_recipes.display_altair import show, Output
from vega_datasets import data
width=700
show(
    boxplot(data.iris(), columns="petalLength", group_by="species", width=width),
    output=Output.pweave_html,
)
```


<script src="https://cdn.jsdelivr.net/npm/vega@3"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@2"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@3"></script>
 <div id="A63597923c7ecec7ccf7f4836d88b9b3a5ac50b068edadfd2f60e93ff1cab2fcd"></div>
  <script type="text/javascript">
    var spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v2.6.0.json",
  "config": {
    "view": {
      "height": 300,
      "width": 400
    }
  },
  "data": {
    "name": "data-a264acbd6e539a8b3afc0cb5f240fb57"
  },
  "datasets": {
    "data-a264acbd6e539a8b3afc0cb5f240fb57": [
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 5.1,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 4.9,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.2,
        "sepalLength": 4.7,
        "sepalWidth": 3.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 4.6,
        "sepalWidth": 3.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 5.0,
        "sepalWidth": 3.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "petalWidth": 0.4,
        "sepalLength": 5.4,
        "sepalWidth": 3.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 4.6,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 5.0,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 4.4,
        "sepalWidth": 2.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.1,
        "sepalLength": 4.9,
        "sepalWidth": 3.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 5.4,
        "sepalWidth": 3.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.2,
        "sepalLength": 4.8,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.1,
        "sepalLength": 4.8,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.1,
        "petalWidth": 0.1,
        "sepalLength": 4.3,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.2,
        "petalWidth": 0.2,
        "sepalLength": 5.8,
        "sepalWidth": 4.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.4,
        "sepalLength": 5.7,
        "sepalWidth": 4.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.4,
        "sepalLength": 5.4,
        "sepalWidth": 3.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 5.1,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 5.7,
        "sepalWidth": 3.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 5.1,
        "sepalWidth": 3.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "petalWidth": 0.2,
        "sepalLength": 5.4,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.4,
        "sepalLength": 5.1,
        "sepalWidth": 3.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.0,
        "petalWidth": 0.2,
        "sepalLength": 4.6,
        "sepalWidth": 3.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "petalWidth": 0.5,
        "sepalLength": 5.1,
        "sepalWidth": 3.3,
        "species": "setosa"
      },
      {
        "petalLength": 1.9,
        "petalWidth": 0.2,
        "sepalLength": 4.8,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.2,
        "sepalLength": 5.0,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.4,
        "sepalLength": 5.0,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 5.2,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 5.2,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.2,
        "sepalLength": 4.7,
        "sepalWidth": 3.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.2,
        "sepalLength": 4.8,
        "sepalWidth": 3.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.4,
        "sepalLength": 5.4,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.1,
        "sepalLength": 5.2,
        "sepalWidth": 4.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 5.5,
        "sepalWidth": 4.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 4.9,
        "sepalWidth": 3.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.2,
        "petalWidth": 0.2,
        "sepalLength": 5.0,
        "sepalWidth": 3.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.2,
        "sepalLength": 5.5,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.1,
        "sepalLength": 4.9,
        "sepalWidth": 3.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.2,
        "sepalLength": 4.4,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 5.1,
        "sepalWidth": 3.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 5.0,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 4.5,
        "sepalWidth": 2.3,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "petalWidth": 0.2,
        "sepalLength": 4.4,
        "sepalWidth": 3.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.6000000000000001,
        "sepalLength": 5.0,
        "sepalWidth": 3.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.9,
        "petalWidth": 0.4,
        "sepalLength": 5.1,
        "sepalWidth": 3.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.30000000000000004,
        "sepalLength": 4.8,
        "sepalWidth": 3.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "petalWidth": 0.2,
        "sepalLength": 5.1,
        "sepalWidth": 3.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 4.6,
        "sepalWidth": 3.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "petalWidth": 0.2,
        "sepalLength": 5.3,
        "sepalWidth": 3.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "petalWidth": 0.2,
        "sepalLength": 5.0,
        "sepalWidth": 3.3,
        "species": "setosa"
      },
      {
        "petalLength": 4.7,
        "petalWidth": 1.4,
        "sepalLength": 7.0,
        "sepalWidth": 3.2,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.5,
        "sepalLength": 6.4,
        "sepalWidth": 3.2,
        "species": "versicolor"
      },
      {
        "petalLength": 4.9,
        "petalWidth": 1.5,
        "sepalLength": 6.9,
        "sepalWidth": 3.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "petalWidth": 1.3,
        "sepalLength": 5.5,
        "sepalWidth": 2.3,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "petalWidth": 1.5,
        "sepalLength": 6.5,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.3,
        "sepalLength": 5.7,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "petalWidth": 1.6,
        "sepalLength": 6.3,
        "sepalWidth": 3.3,
        "species": "versicolor"
      },
      {
        "petalLength": 3.3,
        "petalWidth": 1.0,
        "sepalLength": 4.9,
        "sepalWidth": 2.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "petalWidth": 1.3,
        "sepalLength": 6.6,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "petalWidth": 1.4,
        "sepalLength": 5.2,
        "sepalWidth": 2.7,
        "species": "versicolor"
      },
      {
        "petalLength": 3.5,
        "petalWidth": 1.0,
        "sepalLength": 5.0,
        "sepalWidth": 2.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "petalWidth": 1.5,
        "sepalLength": 5.9,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "petalWidth": 1.0,
        "sepalLength": 6.0,
        "sepalWidth": 2.2,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "petalWidth": 1.4,
        "sepalLength": 6.1,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 3.6,
        "petalWidth": 1.3,
        "sepalLength": 5.6,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "petalWidth": 1.4,
        "sepalLength": 6.7,
        "sepalWidth": 3.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.5,
        "sepalLength": 5.6,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "petalWidth": 1.0,
        "sepalLength": 5.8,
        "sepalWidth": 2.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.5,
        "sepalLength": 6.2,
        "sepalWidth": 2.2,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "petalWidth": 1.1,
        "sepalLength": 5.6,
        "sepalWidth": 2.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.8,
        "petalWidth": 1.8,
        "sepalLength": 5.9,
        "sepalWidth": 3.2,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "petalWidth": 1.3,
        "sepalLength": 6.1,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.9,
        "petalWidth": 1.5,
        "sepalLength": 6.3,
        "sepalWidth": 2.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "petalWidth": 1.2,
        "sepalLength": 6.1,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.3,
        "petalWidth": 1.3,
        "sepalLength": 6.4,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "petalWidth": 1.4,
        "sepalLength": 6.6,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.8,
        "petalWidth": 1.4,
        "sepalLength": 6.8,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 5.0,
        "petalWidth": 1.7000000000000002,
        "sepalLength": 6.7,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.5,
        "sepalLength": 6.0,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 3.5,
        "petalWidth": 1.0,
        "sepalLength": 5.7,
        "sepalWidth": 2.6,
        "species": "versicolor"
      },
      {
        "petalLength": 3.8,
        "petalWidth": 1.1,
        "sepalLength": 5.5,
        "sepalWidth": 2.4,
        "species": "versicolor"
      },
      {
        "petalLength": 3.7,
        "petalWidth": 1.0,
        "sepalLength": 5.5,
        "sepalWidth": 2.4,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "petalWidth": 1.2,
        "sepalLength": 5.8,
        "sepalWidth": 2.7,
        "species": "versicolor"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 1.6,
        "sepalLength": 6.0,
        "sepalWidth": 2.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.5,
        "sepalLength": 5.4,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.6,
        "sepalLength": 6.0,
        "sepalWidth": 3.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "petalWidth": 1.5,
        "sepalLength": 6.7,
        "sepalWidth": 3.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "petalWidth": 1.3,
        "sepalLength": 6.3,
        "sepalWidth": 2.3,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "petalWidth": 1.3,
        "sepalLength": 5.6,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "petalWidth": 1.3,
        "sepalLength": 5.5,
        "sepalWidth": 2.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "petalWidth": 1.2,
        "sepalLength": 5.5,
        "sepalWidth": 2.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "petalWidth": 1.4,
        "sepalLength": 6.1,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "petalWidth": 1.2,
        "sepalLength": 5.8,
        "sepalWidth": 2.6,
        "species": "versicolor"
      },
      {
        "petalLength": 3.3,
        "petalWidth": 1.0,
        "sepalLength": 5.0,
        "sepalWidth": 2.3,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "petalWidth": 1.3,
        "sepalLength": 5.6,
        "sepalWidth": 2.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "petalWidth": 1.2,
        "sepalLength": 5.7,
        "sepalWidth": 3.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "petalWidth": 1.3,
        "sepalLength": 5.7,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.3,
        "petalWidth": 1.3,
        "sepalLength": 6.2,
        "sepalWidth": 2.9,
        "species": "versicolor"
      },
      {
        "petalLength": 3.0,
        "petalWidth": 1.1,
        "sepalLength": 5.1,
        "sepalWidth": 2.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "petalWidth": 1.3,
        "sepalLength": 5.7,
        "sepalWidth": 2.8,
        "species": "versicolor"
      },
      {
        "petalLength": 6.0,
        "petalWidth": 2.5,
        "sepalLength": 6.3,
        "sepalWidth": 3.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 1.9,
        "sepalLength": 5.8,
        "sepalWidth": 2.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.9,
        "petalWidth": 2.1,
        "sepalLength": 7.1,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 1.8,
        "sepalLength": 6.3,
        "sepalWidth": 2.9,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "petalWidth": 2.2,
        "sepalLength": 6.5,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 6.6,
        "petalWidth": 2.1,
        "sepalLength": 7.6,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 4.5,
        "petalWidth": 1.7000000000000002,
        "sepalLength": 4.9,
        "sepalWidth": 2.5,
        "species": "virginica"
      },
      {
        "petalLength": 6.3,
        "petalWidth": 1.8,
        "sepalLength": 7.3,
        "sepalWidth": 2.9,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "petalWidth": 1.8,
        "sepalLength": 6.7,
        "sepalWidth": 2.5,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "petalWidth": 2.5,
        "sepalLength": 7.2,
        "sepalWidth": 3.6,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 2.0,
        "sepalLength": 6.5,
        "sepalWidth": 3.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.3,
        "petalWidth": 1.9,
        "sepalLength": 6.4,
        "sepalWidth": 2.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "petalWidth": 2.1,
        "sepalLength": 6.8,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "petalWidth": 2.0,
        "sepalLength": 5.7,
        "sepalWidth": 2.5,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 2.4,
        "sepalLength": 5.8,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.3,
        "petalWidth": 2.3,
        "sepalLength": 6.4,
        "sepalWidth": 3.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "petalWidth": 1.8,
        "sepalLength": 6.5,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 6.7,
        "petalWidth": 2.2,
        "sepalLength": 7.7,
        "sepalWidth": 3.8,
        "species": "virginica"
      },
      {
        "petalLength": 6.9,
        "petalWidth": 2.3,
        "sepalLength": 7.7,
        "sepalWidth": 2.6,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "petalWidth": 1.5,
        "sepalLength": 6.0,
        "sepalWidth": 2.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "petalWidth": 2.3,
        "sepalLength": 6.9,
        "sepalWidth": 3.2,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "petalWidth": 2.0,
        "sepalLength": 5.6,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 6.7,
        "petalWidth": 2.0,
        "sepalLength": 7.7,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "petalWidth": 1.8,
        "sepalLength": 6.3,
        "sepalWidth": 2.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "petalWidth": 2.1,
        "sepalLength": 6.7,
        "sepalWidth": 3.3,
        "species": "virginica"
      },
      {
        "petalLength": 6.0,
        "petalWidth": 1.8,
        "sepalLength": 7.2,
        "sepalWidth": 3.2,
        "species": "virginica"
      },
      {
        "petalLength": 4.8,
        "petalWidth": 1.8,
        "sepalLength": 6.2,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "petalWidth": 1.8,
        "sepalLength": 6.1,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 2.1,
        "sepalLength": 6.4,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "petalWidth": 1.6,
        "sepalLength": 7.2,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "petalWidth": 1.9,
        "sepalLength": 7.4,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 6.4,
        "petalWidth": 2.0,
        "sepalLength": 7.9,
        "sepalWidth": 3.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 2.2,
        "sepalLength": 6.4,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 1.5,
        "sepalLength": 6.3,
        "sepalWidth": 2.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 1.4,
        "sepalLength": 6.1,
        "sepalWidth": 2.6,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "petalWidth": 2.3,
        "sepalLength": 7.7,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 2.4,
        "sepalLength": 6.3,
        "sepalWidth": 3.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "petalWidth": 1.8,
        "sepalLength": 6.4,
        "sepalWidth": 3.1,
        "species": "virginica"
      },
      {
        "petalLength": 4.8,
        "petalWidth": 1.8,
        "sepalLength": 6.0,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.4,
        "petalWidth": 2.1,
        "sepalLength": 6.9,
        "sepalWidth": 3.1,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "petalWidth": 2.4,
        "sepalLength": 6.7,
        "sepalWidth": 3.1,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 2.3,
        "sepalLength": 6.9,
        "sepalWidth": 3.1,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 1.9,
        "sepalLength": 5.8,
        "sepalWidth": 2.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.9,
        "petalWidth": 2.3,
        "sepalLength": 6.8,
        "sepalWidth": 3.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "petalWidth": 2.5,
        "sepalLength": 6.7,
        "sepalWidth": 3.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.2,
        "petalWidth": 2.3,
        "sepalLength": 6.7,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "petalWidth": 1.9,
        "sepalLength": 6.3,
        "sepalWidth": 2.5,
        "species": "virginica"
      },
      {
        "petalLength": 5.2,
        "petalWidth": 2.0,
        "sepalLength": 6.5,
        "sepalWidth": 3.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.4,
        "petalWidth": 2.3,
        "sepalLength": 6.2,
        "sepalWidth": 3.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "petalWidth": 1.8,
        "sepalLength": 5.9,
        "sepalWidth": 3.0,
        "species": "virginica"
      }
    ]
  },
  "layer": [
    {
      "encoding": {
        "x": {
          "field": "species",
          "type": "nominal"
        },
        "y": {
          "aggregate": "min",
          "axis": {
            "title": "petalLength"
          },
          "field": "petalLength",
          "type": "quantitative"
        },
        "y2": {
          "aggregate": "max",
          "field": "petalLength",
          "type": "quantitative"
        }
      },
      "height": 600,
      "mark": "rule",
      "width": 700
    },
    {
      "encoding": {
        "x": {
          "field": "species",
          "type": "nominal"
        },
        "y": {
          "aggregate": "min",
          "field": "petalLength",
          "type": "quantitative"
        }
      },
      "height": 600,
      "mark": "tick",
      "width": 700
    },
    {
      "encoding": {
        "x": {
          "field": "species",
          "type": "nominal"
        },
        "y": {
          "aggregate": "max",
          "field": "petalLength",
          "type": "quantitative"
        }
      },
      "height": 600,
      "mark": "tick",
      "width": 700
    },
    {
      "encoding": {
        "x": {
          "field": "species",
          "type": "nominal"
        },
        "y": {
          "aggregate": "q1",
          "field": "petalLength",
          "type": "quantitative"
        },
        "y2": {
          "aggregate": "median",
          "field": "petalLength",
          "type": "quantitative"
        }
      },
      "height": 600,
      "mark": {
        "fill": "#4682b4",
        "stroke": "black",
        "type": "bar"
      },
      "width": 700
    },
    {
      "encoding": {
        "x": {
          "field": "species",
          "type": "nominal"
        },
        "y": {
          "aggregate": "median",
          "field": "petalLength",
          "type": "quantitative"
        },
        "y2": {
          "aggregate": "q3",
          "field": "petalLength",
          "type": "quantitative"
        }
      },
      "height": 600,
      "mark": {
        "fill": "#4682b4",
        "stroke": "black",
        "type": "bar"
      },
      "width": 700
    }
  ]
};
    var opt = {"renderer": "canvas", "actions": false};
    vegaEmbed("#A63597923c7ecec7ccf7f4836d88b9b3a5ac50b068edadfd2f60e93ff1cab2fcd", spec, opt);
  </script>
  


(The `show` call is only for compatibility with my publishing pipeline &mdash; skip if you are developing in a notebook or any IPython-kernel-based environment such as the atom extension [Hydrogen](https://atom.io/packages/hydrogen)).

There are many reasons why we may want to do so:

*   It's a well known type of statistical graphics that everyone can recognize and understand on the fly.
*   Creativity is nice, in statistical graphics as in many other endeavors, but dangerous: there are plenty of [bad charts](https://www.google.com/search?q=chartjunk&tbm=isch) out there. The *grammar of graphics* is no insurance.
*   While it's simple to put together a boxplot in `altair`, it isn't trivial: there are rectangles, vertical lines, horizontal lines (whiskers), points (outliers). Each element is related to a different statistics of the data. It's about [30 lines of code](https://altair-viz.github.io/gallery/boxplot_max_min.html) and, unless you run them, it's hard to tell what you are looking at.
*   One doesn't always need the control that the grammar of graphics affords. There are times when I need to see a plot as quickly as possible. Others, for instance preparing a publication, when I need to control every detail.

The boxplot is not the only example. The scatterplot, the quantile-quantile plot, the heatmap are important idioms that are battle tested in data analysis practice. They deserve their own abstraction. Other packages offering an abstraction above the grammar level are:

*   `seaborn` and the graphical subset of `pandas`, for example, both provide high level statistical graphics primitives (higher than the grammar of graphics) and they are quite successful (but not web-based or interactive).
*   `ggplot`, even if named after the Grammar of Graphics, slipped in some more complex charts, pretending they are elements of the grammar, such as `geom_boxplot`, because sometimes even R developers are lazy. But a boxplot is not a *geom*   or mark. It's a combination of several ones, certain statistics and so on. I suspect the authors of `altair` know better than mixing the two levels (but `vega` has not avoided this [trap](https://vega.github.io/vega-lite/docs/boxplot.html), unfortunately).

`altair_recipes` aims to fill this space above `altair` while making full use of its features. It provides a growing list of "classic" statistical graphics without going down to the grammar level. At the same time it is hoped that, over time, it can become  a repository of examples and model best practices for `altair`, a computable form of its [gallery](https://altair-viz.github.io/gallery/index.html). In no way it is a replacement for `altair`: it trades power for convenience and tries to place itself at the highest possible level of abstraction. This is a list of chart types currently available:

*   autocorrelation
*   barchart
*   boxplot
*   heatmap
*   histogram, in a simple and multi-variable version
*   qqplot
*   scatterplot in the simple and all-vs-all versions
*   smoother, smoothing line with IRQ range shading
*   stripplot

You can see all of them in action in the [Examples](https://altair-recipes.readthedocs.io/en/latest/examples.html) section of the documentation. The plan is to carefully expand this list over time with widely used chart types that fulfill a need, as opposed to aiming for an unattainable goal of completeness or indulging in originality for its own sake. Feedback and contributions are welcome.

Other features that promote ease of use are:

*   a highly consistent API enforced with [autosig](http://github.com/piccolbo/autosig);
*   support for both wide and long format;
*   data can be provided as a dataframe or as a URL pointing to a csv or json file, just as in `altair`;
*   all charts produced are valid `altair` charts, can be modified, combined, saved, served, embedded exactly as one;
*   free software under BSD license.

## Choosing a chart type.

It's nice to have all these famous chart types available as one-liners, but we still have to decide which type of graphics to use and, in certain cases, the association between variables in the data and channels in the graphics (what becomes coordinate, what becomes color etc.). It still is work and things can still go wrong, sometimes in subtle ways. Enter `autoplot`. `autoplot` inspects the data, selects a suitable graphics and generates it. While no claim is made that the result is optimal, it will make reasonable choices and avoid common pitfalls, like [overlapping points](https://liorpachter.files.wordpress.com/2017/08/animerr.gif?w=490) in scatterplots. While there are interesting [research efforts](https://github.com/uwdata/draco) aimed at characterizing the optimal graphics for a given data set, their goal is more ambitious than just selecting from a repertoire of pre-defined chart types and they are fairly complex. Therefore, at this time `autoplot` is based on a set of reasonable heuristics derived from decades of experience such as:

*   use stripplot and scatterplot to display continuous data, barcharts for discrete data
*   use opacity to counter mark overlap, but not with discrete color maps
*   switch to summaries (count and averages) when the amount of overlap is too high
*   use facets for discrete data.

In the following examples, we just have to provide `autoplot` with a dataset and a list of columns to plot. The result is a scatterplot faceted w.r.t. the only discrete column.


```python
from altair_recipes import autoplot

show(
    autoplot(data.iris(), columns=["petalLength", "sepalLength", "species"], width=width),
    output=Output.pweave_html,
)
```


<div id="A44ee3a76f7f8a0abe6fbae6871933382598aef532120f8c21a1b1d6a24815662"></div>
  <script type="text/javascript">
    var spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v2.6.0.json",
  "config": {
    "view": {
      "height": 300,
      "width": 400
    }
  },
  "data": {
    "name": "data-60832c4f15b276d133fd10d3bd19dc33"
  },
  "datasets": {
    "data-60832c4f15b276d133fd10d3bd19dc33": [
      {
        "petalLength": 1.4,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 4.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 4.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 4.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 4.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.1,
        "sepalLength": 4.3,
        "species": "setosa"
      },
      {
        "petalLength": 1.2,
        "sepalLength": 5.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "sepalLength": 5.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.0,
        "sepalLength": 4.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.7000000000000002,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.9,
        "sepalLength": 4.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 4.7,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 4.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.2,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 4.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.2,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 5.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.9,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 4.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 4.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 4.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 1.9,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.8,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 4.6,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.3,
        "species": "setosa"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 7.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.9,
        "sepalLength": 6.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "sepalLength": 6.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.3,
        "species": "versicolor"
      },
      {
        "petalLength": 3.3,
        "sepalLength": 4.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "sepalLength": 6.6,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "sepalLength": 5.2,
        "species": "versicolor"
      },
      {
        "petalLength": 3.5,
        "sepalLength": 5.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "sepalLength": 5.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 6.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.1,
        "species": "versicolor"
      },
      {
        "petalLength": 3.6,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 6.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "sepalLength": 5.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.2,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.8,
        "sepalLength": 5.9,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 6.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.9,
        "sepalLength": 6.3,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.3,
        "sepalLength": 6.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 6.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.8,
        "sepalLength": 6.8,
        "species": "versicolor"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 6.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.0,
        "species": "versicolor"
      },
      {
        "petalLength": 3.5,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 3.8,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 3.7,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 3.9,
        "sepalLength": 5.8,
        "species": "versicolor"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 6.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 5.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 6.3,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.6,
        "sepalLength": 6.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 5.8,
        "species": "versicolor"
      },
      {
        "petalLength": 3.3,
        "sepalLength": 5.0,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.2,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 4.3,
        "sepalLength": 6.2,
        "species": "versicolor"
      },
      {
        "petalLength": 3.0,
        "sepalLength": 5.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.1,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 6.0,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 5.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.9,
        "sepalLength": 7.1,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "sepalLength": 6.5,
        "species": "virginica"
      },
      {
        "petalLength": 6.6,
        "sepalLength": 7.6,
        "species": "virginica"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 4.9,
        "species": "virginica"
      },
      {
        "petalLength": 6.3,
        "sepalLength": 7.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "sepalLength": 6.7,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "sepalLength": 7.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 6.5,
        "species": "virginica"
      },
      {
        "petalLength": 5.3,
        "sepalLength": 6.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "sepalLength": 6.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 5.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 5.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.3,
        "sepalLength": 6.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "sepalLength": 6.5,
        "species": "virginica"
      },
      {
        "petalLength": 6.7,
        "sepalLength": 7.7,
        "species": "virginica"
      },
      {
        "petalLength": 6.9,
        "sepalLength": 7.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 6.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "sepalLength": 6.9,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "sepalLength": 5.6,
        "species": "virginica"
      },
      {
        "petalLength": 6.7,
        "sepalLength": 7.7,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "sepalLength": 6.7,
        "species": "virginica"
      },
      {
        "petalLength": 6.0,
        "sepalLength": 7.2,
        "species": "virginica"
      },
      {
        "petalLength": 4.8,
        "sepalLength": 6.2,
        "species": "virginica"
      },
      {
        "petalLength": 4.9,
        "sepalLength": 6.1,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.8,
        "sepalLength": 7.2,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "sepalLength": 7.4,
        "species": "virginica"
      },
      {
        "petalLength": 6.4,
        "sepalLength": 7.9,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.4,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.1,
        "species": "virginica"
      },
      {
        "petalLength": 6.1,
        "sepalLength": 7.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.5,
        "sepalLength": 6.4,
        "species": "virginica"
      },
      {
        "petalLength": 4.8,
        "sepalLength": 6.0,
        "species": "virginica"
      },
      {
        "petalLength": 5.4,
        "sepalLength": 6.9,
        "species": "virginica"
      },
      {
        "petalLength": 5.6,
        "sepalLength": 6.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 6.9,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 5.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.9,
        "sepalLength": 6.8,
        "species": "virginica"
      },
      {
        "petalLength": 5.7,
        "sepalLength": 6.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.2,
        "sepalLength": 6.7,
        "species": "virginica"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 6.3,
        "species": "virginica"
      },
      {
        "petalLength": 5.2,
        "sepalLength": 6.5,
        "species": "virginica"
      },
      {
        "petalLength": 5.4,
        "sepalLength": 6.2,
        "species": "virginica"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 5.9,
        "species": "virginica"
      }
    ]
  },
  "facet": {
    "row": {
      "field": "species",
      "type": "nominal"
    }
  },
  "spec": {
    "encoding": {
      "x": {
        "field": "sepalLength",
        "type": "quantitative"
      },
      "y": {
        "field": "petalLength",
        "type": "quantitative"
      }
    },
    "height": 200,
    "mark": {
      "opacity": 0.3333333333333333,
      "type": "circle"
    },
    "width": 233
  }
};
    var opt = {"renderer": "canvas", "actions": false};
    vegaEmbed("#A44ee3a76f7f8a0abe6fbae6871933382598aef532120f8c21a1b1d6a24815662", spec, opt);
  </script>
  

Opacity is used to prevent some points from completely hiding others. Opacity and discrete color scales don't mix well, hence the use of faceting. In fact, just by displaying a subset of points, we can see the plot type adapt with no other change in the `autoplot` call.


```python

show(
    autoplot(
        data.iris().sample(30, random_state=1),
        columns=["petalLength", "sepalLength", "species"],
        width=width,
    ),
    output=Output.pweave_html,
)
```


<div id="A71caa65f865118a83bbe26bb55c7e065784aed47fe88bd4add7c251ab03ef0ac"></div>
  <script type="text/javascript">
    var spec = {
  "$schema": "https://vega.github.io/schema/vega-lite/v2.6.0.json",
  "config": {
    "view": {
      "height": 300,
      "width": 400
    }
  },
  "data": {
    "name": "data-3448e024270005cbe8084ef545c262d7"
  },
  "datasets": {
    "data-3448e024270005cbe8084ef545c262d7": [
      {
        "petalLength": 1.2,
        "sepalLength": 5.8,
        "species": "setosa"
      },
      {
        "petalLength": 3.0,
        "sepalLength": 5.1,
        "species": "versicolor"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 6.6,
        "species": "versicolor"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 6.4,
        "sepalLength": 7.9,
        "species": "virginica"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.3,
        "species": "versicolor"
      },
      {
        "petalLength": 5.1,
        "sepalLength": 6.9,
        "species": "virginica"
      },
      {
        "petalLength": 1.9,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 1.6,
        "sepalLength": 4.7,
        "species": "setosa"
      },
      {
        "petalLength": 5.7,
        "sepalLength": 6.9,
        "species": "virginica"
      },
      {
        "petalLength": 4.2,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 1.7000000000000002,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 5.9,
        "sepalLength": 7.1,
        "species": "virginica"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.4,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 6.0,
        "species": "versicolor"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 4.4,
        "species": "setosa"
      },
      {
        "petalLength": 4.0,
        "sepalLength": 5.8,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 5.6,
        "species": "versicolor"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.4,
        "species": "setosa"
      },
      {
        "petalLength": 1.2,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 4.4,
        "sepalLength": 5.5,
        "species": "versicolor"
      },
      {
        "petalLength": 4.5,
        "sepalLength": 5.4,
        "species": "versicolor"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 6.7,
        "species": "versicolor"
      },
      {
        "petalLength": 1.3,
        "sepalLength": 5.0,
        "species": "setosa"
      },
      {
        "petalLength": 6.0,
        "sepalLength": 7.2,
        "species": "virginica"
      },
      {
        "petalLength": 4.1,
        "sepalLength": 5.7,
        "species": "versicolor"
      },
      {
        "petalLength": 1.4,
        "sepalLength": 5.5,
        "species": "setosa"
      },
      {
        "petalLength": 1.5,
        "sepalLength": 5.1,
        "species": "setosa"
      },
      {
        "petalLength": 4.7,
        "sepalLength": 6.1,
        "species": "versicolor"
      },
      {
        "petalLength": 5.0,
        "sepalLength": 6.3,
        "species": "virginica"
      }
    ]
  },
  "encoding": {
    "color": {
      "field": "species",
      "type": "nominal"
    },
    "x": {
      "field": "sepalLength",
      "type": "quantitative"
    },
    "y": {
      "field": "petalLength",
      "type": "quantitative"
    }
  },
  "height": 600,
  "mark": {
    "opacity": 1.0,
    "type": "point"
  },
  "width": 700
};
    var opt = {"renderer": "canvas", "actions": false};
    vegaEmbed("#A71caa65f865118a83bbe26bb55c7e065784aed47fe88bd4add7c251ab03ef0ac", spec, opt);
  </script>
  


With minimal overlap between points, there is no need to use opacity, which allows to represent the species with color as opposed to faceting. This also allows to keep the chart bigger (but size can also be specified by the user).

`autoplot` is work in progress and perhaps will always be and feedback is most welcome. A large number of charts generated with it is available at the end of the [Examples](https://altair-recipes.readthedocs.io/en/latest/examples.html) page and should give a good idea of what it does. In particular, in this first iteration, we do not make any attempt to detect if a dataset represents a function or a relation, hence scatterplots are preferred over line plots. Moreover there is no support for:

*   evenly spaced data, such as a time series;
*   more than 3 variables being plotted at the same time;
*   additional channels such as size, shape and text.

There is no fundamental reason why these features are not included. Suggestions and contributions are welcome.

## Quality

Quality in software is often a matter of opinion, but that's no reason to skip the few measurable activities that improve code quality:

*   [Fully documented](https://altair_recipes.readthedocs.io).
*   Continuos [integration](https://travis-ci.org/piccolbo/altair_recipes)
*   Near 100% regression test [coverage](https://codecov.io/gh/piccolbo/altair_recipes).
*   B maintainability score according to [Codeclimate](https://codeclimate.com/github/piccolbo/altair_recipes). We miss the top mark because the API is "flat", which brings about some function argument inflation. Most have defaults, though.
*   Dependencies checked with pyup.

## Conclusion

If you are interested in interactive statistical graphics for the web in python and in particular if you are already using `altair`, `altair_recipes` is the path of least resistance to producing the most common plot types. Check it out and feel free to create an [issue](https://github.com/piccolbo/altair_recipes/issues) reporting problems or suggesting features. Or, better yet, come help with development!
