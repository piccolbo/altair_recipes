#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    "altair>=3.2.0",
    "autosig>=0.7.0",
    "boltons>=19.1.0",
    "ipython==6.5.0",
    "numpy>=1.17.0",
    "pandas>=0.25.0",
    "requests>=2.22.0",
    "toolz>=0.10.0",
]

setup_requirements = ['pytest-runner']

test_requirements = ['pytest']

setup(
    author="Antonio Piccolboni",
    author_email='antonio@piccolboni.info',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A collection of ready-made statistical graphics for vega",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='altair_recipes',
    name='altair_recipes',
    packages=find_packages(include=['altair_recipes']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/piccolbo/altair_recipes',
    version='0.6.0',
    zip_safe=False,
)
