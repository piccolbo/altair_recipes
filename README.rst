
Introduction to altair_recipes
==============================


.. image:: https://img.shields.io/pypi/v/altair_recipes.svg
        :target: https://pypi.python.org/pypi/altair_recipes
        :alt: Version

.. image:: https://codecov.io/gh/piccolbo/altair_recipes/graph/badge.svg
        :target: https://codecov.io/gh/piccolbo/altair_recipes
        :alt: Code Coverage

.. image:: https://readthedocs.org/projects/altair_recipes/badge/?version=latest
        :target: https://altair_recipes.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/piccolbo/altair_recipes/shield.svg
     :target: https://pyup.io/repos/github/piccolbo/altair_recipes/
     :alt: Updates

.. image:: https://api.codeclimate.com/v1/badges/4ab3f4aad65b12b2bb7c/maintainability
     :target: https://codeclimate.com/github/piccolbo/altair_recipes/maintainability
     :alt: Maintainability


A collection of ready-made statistical graphics for vega.
---------------------------------------------------------

``vega`` is a statistical graphics system for the web, meaning the plots are displayed in a browser. As an added bonus, it adds interactions, again through web technologies: select data point, reveal information on hover etc. Interaction and the web are clearly the future of statistical graphics. Even the successor to the famous ``ggplot`` for R, ``ggvis`` is based on ``vega``.

``altair`` is a python package that produces ``vega`` graphics. Like ``vega``, it adopts an approach to describing statistical graphics known as *grammar of graphics* which underlies other well known packages such as ``ggplot`` for R. It represents a extremely useful compromise of power and flexibility. Its elements are data, marks (points, lines), encodings (relations between data and marks), scales etc.

Sometimes we want to skip all of that and just produce a boxplot (or heatmap or histogram, the argument is the same) by calling::

  boxplot(data.iris(), columns="petalLength", group_by="species")

because:


* It's a well known type of statistical graphics that everyone can recognize and understand on the fly.
* Creativity is nice, in statistical graphics as in many other endeavors, but dangerous: there are more `bad charts <https://www.google.com/search?q=chartjunk&tbm=isch>`_ out there than good ones. The *grammar of graphics* is no insurance.
* While it's simple to put together a boxplot in ``altair``, it isn't trivial: there are rectangles, vertical lines, horizontal lines (whiskers), points (outliers). Each element is related to a different statistics of the data. It's about `30 lines of code <https://altair-viz.github.io/gallery/boxplot_max_min.html>`_ and, unless you run them, it's hard to tell you are looking at a boxplot.
* One doesn't always need the control that the grammar of graphics affords. There are times when I need to see a boxplot as quick as possible. Others, for instance preparing a publication, when I need to control every detail.

The boxplot is not the only example. The scatterplot, the quantile-quantile plot, the heatmap are important idioms that are battle tested in data analysis practice. They deserve their own abstraction. Other packages offering an abstraction above the grammar level are:

* ``seaborn`` and the graphical subset of ``pandas``, for example, both provide high level statistical graphics primitives (higher than the grammar of graphics) and they are quite successful (but not web-based).
* ``ggplot``, even if named after the Grammar of Graphics, slipped in some more complex charts, pretending they are elements of the grammar, such as ``geom_boxplot``, because sometimes even R developers are lazy. But a boxplot is not a *geom* or mark. It's a combination of several ones, certain statistics and so on. I suspect the authors of ``altair`` know better than mixing the two levels.


``altair_recipes`` aims to fill this space above ``altair`` while making full use of its features. It provides a growing list of "classic" statistical graphics without going down to the grammar level. At the same time it is hoped that, over time, it can become  a repository of examples and model best practices for ``altair``, a computable form of its `gallery <https://altair-viz.github.io/gallery/index.html>`_.

There is *one more thing*. It's nice to have all these famous chart types available at a stroke of the keyboard, but we still have to decide which type of graphics to use and, in certain cases, the association between variables in the data and channels in the graphics (what becomes coordinate, what becomes color etc.). It still is work and things can still go wrong, sometimes in subtle ways. Enter ``autoplot``. ``autoplot`` inspects the data, selects a suitable graphics and generates it. While no claim is made that the result is optimal, it will make reasonable choices and avoid common pitfalls, like `overlapping points <https://liorpachter.files.wordpress.com/2017/08/animerr.gif?w=490>`_ in scatterplots. While there are interesting `research efforts <https://github.com/uwdata/draco>`_ aimed at characterizing the optimal graphics for a given data set, their goal is more ambitious than just selecting from a repertoire of pre-defined graphics types and they are fairly complex. Therefore, at this time ``autoplot`` is based on a set of reasonable heuristics derived from decades of experience such as:

* use stripplot and scatterplot to display continuous data, barcharts for discrete data
* use opacity to counter mark overlap, but not with discrete color maps
* switch to summaries (count and averages) when the amount of overlap is too high
* use facets for discrete data

``autoplot`` is work in progress and perhaps will always be and feedback is most welcome. A large number of charts generated with it is available at the end of the Examples_ page and should give a good idea of what it does. In particular, in this first iteration we do not make any attempt to detect if a dataset represents a function or a relation, hence scatterplots are preferred over line plots. Moreover there is no special support for evenly spaced data, such as a time series.

Features
--------

* Free software: BSD license.
* Fully documented_.
* Highly consistent API enforced with autosig_
* Near 100% regression test coverage.
* Support for dataframe and vector inputs
* Support for both wide and long dataframe formats.
* Data can be provided as a dataframe or as a URL pointing to a csv or json file.
* All charts produced are valid ``altair`` charts, can be modified, combined, saved, served, embedded exactly as one.


Chart types
-----------

* autocorrelation
* barchart
* boxplot
* heatmap
* histogram, in a simple and multi-variable version
* qqplot
* scatterplot in the simple and all-vs-all versions
* smoother, smoothing line with IRQ range shading
* stripplot

See Examples_.


.. _Examples: https://altair-recipes.readthedocs.io/en/latest/examples.html
.. _autosig: http://github.com/piccolbo/autosig
.. _documented: https://altair_recipes.readthedocs.io
