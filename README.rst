==============
altair_recipes
==============


.. image:: https://img.shields.io/pypi/v/altair_recipes.svg
        :target: https://pypi.python.org/pypi/altair_recipes
        :alt: Version

.. image:: https://img.shields.io/travis/piccolbo/altair_recipes.svg
        :target: https://travis-ci.org/piccolbo/altair_recipes
        :alt: Build Status

.. image:: https://codecov.io/gh/piccolbo/altair_recipes/graph/badge.svg
        :target: https://codecov.io/gh/piccolbo/altair_recipes
        :alt: Code Coverage

.. image:: https://readthedocs.org/projects/altair_recipes/badge/?version=latest
        :target: https://altair_recipes.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/piccolbo/altair_recipes/shield.svg
     :target: https://pyup.io/repos/github/piccolbo/altair_recipes/
     :alt: Updates



---------------------------------------------------------
A collection of ready-made statistical graphics for vega.
---------------------------------------------------------

``vega`` is a statistical graphics system for the web, meaning the plots are displayed in a browser. As an added bonus, it adds interactions, again through web technologies: select data point, reveal information on hover etc. Interaction and the web are clearly the future of statistical graphics. Even the successor to the famous `ggplot` for R, `ggvis` is based on `vega`.

``altair`` is a python package that produces ``vega`` graphics. Like ``vega``, it adopts an approach to describing statistical graphics known as *grammar of graphics* which underlies other well known packages such as ``ggplot`` for R. It represents a extremely useful compromise of power and flexibility. Its elements are data, marks (points, lines), encodings (relations between data and marks), scales etc.

Sometimes we want to skip all of that and just produce a boxplot (or heatmap or histogram, the argument is the same) by calling ``boxplot(...)`` because:

* It's more convenient, faster, less error-prone.
* It's a well known type of statistical graphics that everyone can recognize and understand on the fly.
* It's widely used and time tested.
* Creativity is nice, in statistical graphics as in many other endeavors, but takes effort: there are more bad charts out there than good ones. Following a grammar won't guarantee a text is a classic novel. A boxplot is beyond reproach.
* While it's simple to put together a boxplot in ``altair``, it isn't trivial: there are rectangles, vertical lines, horizontal lines (whiskers), points (outliers). Each element is related to a different statistics of the data. It's a few lines of code and, unless you run them, it's hard to tell you are looking at a boxplot.
* In software, there is often room for different compromises between power and ease of use, and while the one picked by ``altair`` is incredibly useful and proven over several implementations and years of practice, there are times when you don't need its full power. Just show me a boxplot of the data, I don't care what the whiskers thickness is. It's got to be done by yesterday and no, it's not for a Science submission. Any decent boxplot will do, thanks.
* ``seaborn`` and the graphical subset of ``pandas``, for example, both provide high level statistical graphics primitives (higher than the grammar of graphics) and they are quite successful (but not web-based).
* Even ``ggplot``, which is named after the Grammar of Graphics, slipped in some more complex charts, pretending they are elements of the grammar, such as ``geom_boxplot``, because sometimes even R developers are lazy. But a boxplot is not a *geom* or mark. It's a combination of several ones, certain statistics and so on. The right approach is to keep these two levels of abstraction separate.

The boxplot is not the only example. The scatter plot, the quantile-quantile plot, the heatmap are important idioms that are battle tested in data analysis practice. They deserve their own abstraction.


``altair_recipes`` aims to fill this space above ``altair`` while making full use of its features. It provides a growing list of "classic" statistical graphics without going down to the grammar level. At the same time it is hoped that it can provide examples and model best practices for ``altair``.

And while we were at it, here are some goodies:

* Free software: BSD license.
* Fully documented: https://altair_recipes.readthedocs.io.
* Highly consistent API enforced with autosig_
* Near 100% regression test coverage.
* Most API entrypoints accept data in both wide and long format.
* Data can be provided as a dataframe or as a URL pointing to a csv or json file.
* All charts produced are valid ``altair`` charts, can be modified, combined, saved, served, embedded exactly as one.


Features
--------

* autocorrelation
* boxplot
* heatmap
* histogram, in a simple and multi-variable version
* qqplot
* scatter, in the simple and all-vs-all versions
* smoother, smoothing line with IRQ range shading

See Examples_.

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Examples: https://altair-recipes.readthedocs.io/en/latest/examples.html
.. _autosig: http://github.com/piccolbo/autosig
