=======
History
=======

0.9.0 (2020-06-11)
------------------

* Fixed color in boxplot
* Upgrade to altair 4. Mandatory. Let me know if you need compatibility with 3.x.x

0.8.0 (2019-10-16)
------------------

* Added lineplots and areaplots #11 and #12

0.7.1 (2019-10-07)
------------------

* Accepts vector data in addition to dataframe, as in::

    import altair_recipes as ar
    from numpy.random import normal
    ar.scatterplot(x=normal(size=100), y=normal(size=100))


0.6.5 (2019-10-01)
------------------

* Make ipython dep optional (for pweave support). Use piccolbo's pweave fork (upstream doesn't pass its own tests) for doc generation. Adapt to breaking changes in autosig (a dependency).

0.6.4 (2019-09-18)
------------------

* Switched to poetry for package management

0.6.0 (2019-01-25)
------------------

* Fine tuned API:
    * no faceting but all returned charts are facet-able
    * Color made a bool option when separate color dim can't work
    * Eliminated some special cases from autoplot for very small datasets
    * Some refactor in boxpolot and autoplot to shrink, clarify code


0.5.0 (2019-01-17)
------------------

* Autoplot for automatic statistical graphics
* Stripplots and barcharts

0.4.0 (2018-09-25)
------------------

* Custom height and width for all charts


0.3.2 (2018-09-21)
------------------

* Dealt with breaking changes from autosig, but code is simpler and paves the way for some new features

0.3.1 (2018-09-20)
------------------

* Addressing a documentation mishap

0.3.0 (2018-09-20)
------------------

* Better readme and a raft of examples
* Some test flakiness addressed

0.2.4 (2018-08-29)
------------------

* One more issue with col resolution
* Switch to using docstring support in autosig

0.2.3 (2018-08-29)
------------------

* Some issues with processing of `columns` and `group_by` args
* Fixed travis-ci build (3.6 only, 3.5 looks like a minor RNG issue)

0.2.2 (2018-08-28)
------------------

* Switch to a simpler, flatter API a la qplot
* Added two types of heatmaps
* Extensive use of autosig features for API consistency and reduced boilerplate
* Fixed build to follow requests model (pip for users, pipenv for devs)

0.1.2 (2018-08-14)
------------------

* Fixed a number of loose ends particularly wrt docs


0.1.0 (2018-08-06)
------------------

* First release on PyPI.
