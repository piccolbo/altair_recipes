.. highlight:: shell


Contributing
============

Contributions are welcome, and they are greatly appreciated! Every little bit
helps, and credit will always be given.

You can contribute in many ways:

Types of Contributions
----------------------

Report Bugs
~~~~~~~~~~~

Report bugs at https://github.com/piccolbo/altair_recipes/issues.

If you are reporting a bug, please include:

* Your operating system name and version.
* Any details about your local setup that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

Fix Bugs
~~~~~~~~

Look through the GitHub issues for bugs. Anything tagged with "bug" and "help
wanted" is open to whoever wants to implement it.

Propose Features
~~~~~~~~~~~~~~~~

The types of new features we can think of are of two types. First is more flexibility for charts that altair_recipes can produce already, e.g. the recent addition of height and width controls; second is entirely new types of chars. As to the first, we are trying to balance two aims: keeping it simple and making it powerful enough to cover common visualization needs. This isn't very precise, but we will try to make it  more so over time. Controlling the width seemed a necessity. Changing a color palette, maybe not so much (it can also be controlled with ``altair``'s ``configure_*`` methods). As to entirely new types of chart, we'd like to include any charts that are in widespread use in data analysis practice, which may have a scientific article or a wikipedia entry devoted to them or other supporting evidence of statistical relevance. Chart types that have been used once or are implemented in a single library, like the *jointplot*, are not good candidates. To propose a new feature, please open a new issue with description, rationale, an example and, ideally, sample implementation in ``altair`` or ``vega-lite``.

Implement Features
~~~~~~~~~~~~~~~~~~

Look through the GitHub issues for features. Anything tagged with "enhancement"
and "help wanted" is open to whoever wants to implement it. A new type of chart will require a new test.

Write Documentation
~~~~~~~~~~~~~~~~~~~

altair_recipes could always use more documentation, whether as part of the
official altair_recipes docs, in docstrings, or even on the web in blog posts,
articles, and such.

Submit Feedback
~~~~~~~~~~~~~~~

The best way to send feedback is to file an issue at https://github.com/piccolbo/altair_recipes/issues.

If you are proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.
* Remember that this is a volunteer-only project, and that contributions
 are welcome :)

Get Started!
------------

Ready to contribute? Here's how to set up `altair_recipes` for local development.

1. Fork the `altair_recipes` repo on GitHub.
2. Clone your fork locally::

   $ git clone git@github.com:your_name_here/altair_recipes.git

3. Install your local copy into a virtualenv. This is how you set up your fork for local development::

    $ pip install pipenv #if needed
    $ cd altair_recipes/
    $ pipenv install --dev

4. Create a branch for local development::

    $ git checkout -b <branch-name>

   Where <branch-name> can be as simple as ``issue-<issue-number>`` but should always end with ``-<issue-number>``. Now you can make your changes locally.

5. When you're done making changes, check that your changes pass flake8 and the
   tests, including testing other Python versions with tox::

    $ make test

6. Commit your changes and push your branch to GitHub::

    $ git add .
    $ git commit -m "Your detailed description of your changes."
    $ git push origin <branch-name>

7. Submit a pull request through the GitHub website.

Pull Request Guidelines
-----------------------

Before you submit a pull request, check that it meets these guidelines:

1. The pull request should include tests. Coverage should never decrease
   (check with make coverage)
2. If the pull request adds functionality, the docs should be updated. Put
   your new functionality into a function with a docstring, and add new chat types to the list in README.rst.
3. The pull request should work for Python 3.5 and 3.6, or as listed in file
   travis.yml. Check
   https://travis-ci.org/piccolbo/altair_recipes/pull_requests
   and make sure that the tests pass for all supported Python versions.

Tips
----

To run a subset of tests::

$ py.test tests.test_altair_recipes

Tests should be decorated with ``@viz-reg-test`` and produce an altair chart. This will save the json output for regression testing and produce an html file  for visual inspection.

Deploying
---------

A reminder for the maintainers on how to deploy.
Make sure all your changes are committed (including an entry in HISTORY.rst).
Then run::

$ bumpversion patch # possible: major / minor / patch

We use semantic versioning. Then::

$ git push
$ git push --tags

Travis will then deploy to PyPI if tests pass (not implemented yet, use ``make release``)
