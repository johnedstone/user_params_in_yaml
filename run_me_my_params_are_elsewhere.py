# -*- coding: utf-8 -*-
"""
This file will use the file user_parameters.yaml in some other directory, e.g. in your data directory
"""

from functions import myplot

DEBUG = True

results_one, results_two = myplot.start_plot(user_param='elsewhere')

if DEBUG:
    print(results_one, results_two)

# vim: ai et ts=4 sw=4 sts=4 nu ru
