# -*- coding: utf-8 -*-
"""
This file will use the file functions/user_parameters.py which may have been how you started
"""

from functions import myplot

DEBUG = True

results_one, results_two = myplot.start_plot(user_param='sample')

if DEBUG:
    print(results_one, results_two)

# vim: ai et ts=4 sw=4 sts=4 nu ru
