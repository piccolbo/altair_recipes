# -*- coding: utf-8 -*-
"""Top-level package for altair_recipes."""
from .autocorrelation import autocorrelation
from .autoplot import autoplot
from .barchart import barchart
from .boxplot import boxplot
from .common import layer
from .heatmap import heatmap
from .histogram import histogram, layered_histogram
from .lineplot import lineplot
from .areaplot import areaplot, StackType
from .qqplot import qqplot
from .scatterplot import scatterplot, multiscatterplot
from .smoother import smoother
from .stripplot import stripplot


# alphabetically ordered exports
__all__ = [
    "areaplot",
    "autocorrelation",
    "autoplot",
    "barchart",
    "boxplot",
    "layer",
    "lineplot",
    "heatmap",
    "histogram",
    "layered_histogram",
    "multiscatterplot",
    "qqplot",
    "scatterplot",
    "smoother",
    "StackType",
    "stripplot",
]
__author__ = """Antonio Piccolboni"""
__email__ = "altair_recipes@piccolboni.info"
__version__ = "__version__ = '0.9.1'"
