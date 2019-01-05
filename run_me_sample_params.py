# -*- coding: utf-8 -*-
"""
This file will use the file functions/user_parameters.py which may have been how you started
"""

import logging
import logging.config
import yaml

from functions import myplot

DEBUG = True

with open('functions/my_logger.yaml', 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

if DEBUG:
    logger = logging.getLogger('log_info')
else:
    logger = logging.getLogger('log_warning')

results_one, results_two = myplot.start_plot(user_param='sample')

logger.info('''
    results_one: {}
    results_two: {}
    '''.format(results_one, results_two))

# vim: ai et ts=4 sw=4 sts=4 nu ru
