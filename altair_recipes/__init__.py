# -*- coding: utf-8 -*-
"""Top-level package for altair_recipes."""
from .autocorrelation import autocorrelation
from .boxplot import boxplot
from .heatmap import binned_heatmap
from .heatmap import heatmap
from .histogram import histogram, layered_histogram
from .qqplot import qqplot
from .scatter import scatter, multiscatter
from .smoother import smoother

# alphabetically ordered exports
__all__ = [
    'autocorrelation',
    'binned_heatmap',
    'boxplot',
    'heatmap',
    'histogram',
    'layered_histogram',
    'multiscatter',
    'qqplot',
    'scatter',
    'smoother',
]
__author__ = """Antonio Piccolboni"""
__email__ = 'antonio@piccolboni.info'
__version__ = '0.2.1'
