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

``vega`` is a statistical graphics system for the web, meaning the plots are displayed in a browser. As an added bonus, it adds interactions, again through web technologies: select data point, reveal information on hover etc. Interaction and the web are clearly the future of statistical graphics. Even the successor to the famous ``ggplot`` for R, ``ggvis`` is based on ``vega``.

``altair`` is a python package that produces ``vega`` graphics. Like ``vega``, it adopts an approach to describing statistical graphics known as *grammar of graphics* which underlies other well known packages such as ``ggplot`` for R. It represents a extremely useful compromise of power and flexibility. Its elements are data, marks (points, lines), encodings (relations between data and marks), scales etc.

Sometimes we want to skip all of that and just produce a boxplot (or heatmap or histogram, the argument is the same) by calling::

  boxplot(data.iris(), columns="petalLength", group_by="species")

because:


* It's a well known type of statistical graphics that everyone can recognize and understand on the fly.
* Creativity is nice, in statistical graphics as in many other endeavors, but dangerous: there are more `bad charts <https://www.google.com/search?q=chartjunk&tbm=isch>`_ out there than good ones. The *grammar of graphics* is no insurance.
* While it's simple to put together a boxplot in ``altair``, it isn't trivial: there are rectangles, vertical lines, horizontal lines (whiskers), points (outliers). Each element is related to a different statistics of the data. It's about `30 lines of code <https://altair-viz.github.io/gallery/boxplot_max_min.html>`_ and, unless you run them, it's hard to tell you are looking at a boxplot.
* One doesn't always need the control that the grammar of graphics affords. There are times when I need to see a boxplot as quick as possible. Others, for instance preparing a publication, when I need to control every detail.

The boxplot is not the only example. The scatter plot, the quantile-quantile plot, the heatmap are important idioms that are battle tested in data analysis practice. They deserve their own abstraction. Other packages offering an abstraction above the grammar level are:

* ``seaborn`` and the graphical subset of ``pandas``, for example, both provide high level statistical graphics primitives (higher than the grammar of graphics) and they are quite successful (but not web-based).
* ``ggplot``, even if named after the Grammar of Graphics, slipped in some more complex charts, pretending they are elements of the grammar, such as ``geom_boxplot``, because sometimes even R developers are lazy. But a boxplot is not a *geom* or mark. It's a combination of several ones, certain statistics and so on. I suspect the authors of ``altair`` know better than mixing the two levels.


``altair_recipes`` aims to fill this space above ``altair`` while making full use of its features. It provides a growing list of "classic" statistical graphics without going down to the grammar level. At the same time it is hoped that, over time, it can become  a repository of examples and model best practices for ``altair``, a computable form of its `gallery <https://altair-viz.github.io/gallery/index.html>`_

Features
--------

* Free software: BSD license.
* Fully documented: https://altair_recipes.readthedocs.io.
* Highly consistent API enforced with `autosig <https://github.com/piccolbo/autosig>`_
* Near 100% regression test coverage.
* Support for both wide and long format.
* Data can be provided as a dataframe or as a URL pointing to a csv or json file.
* All charts produced are valid ``altair`` charts, can be modified, combined, saved, served, embedded exactly as one.


Chart types
-----------

* autocorrelation
* boxplot
* heatmap
* histogram, in a simple and multi-variable version
* qqplot
* scatter, in the simple and all-vs-all versions
* smoother, smoothing line with IRQ range shading

See `Examples <https://altair-recipes.readthedocs.io/en/latest/examples.html>`_.

Credits
-------

This package was created with Cookiecutter_ and the `elgertam/cookiecutter-pipenv`_ project template, based on `audreyr/cookiecutter-pypackage`_.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`elgertam/cookiecutter-pipenv`: https://github.com/elgertam/cookiecutter-pipenv
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
.. _Examples: https://altair-recipes.readthedocs.io/en/latest/examples.html
.. _autosig: http://github.com/piccolbo/autosig
