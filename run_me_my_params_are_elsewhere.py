# -*- coding: utf-8 -*-
"""
This file will use the file user_parameters.yaml in some other directory, e.g. in your data directory
"""
import logging
from functions import myplot

DEBUG = True

if DEBUG:
    logging.basicConfig(format='%(levelname)s:%(filename)s:%(lineno)s:%(message)s', level=logging.INFO)

results_one, results_two = myplot.start_plot(user_param='/path/relative/to/home/user_parameters.yaml')

if DEBUG:
    logging.info('''
    results_one: {}
    results_two: {}
    '''.format(results_one, results_two))

# vim: ai et ts=4 sw=4 sts=4 nu ru
