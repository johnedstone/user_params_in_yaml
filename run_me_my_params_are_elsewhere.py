# -*- coding: utf-8 -*-
"""
This file will use the file user_parameters.yaml in some other directory, e.g. in your data directory
"""

import logging
import logging.config
import yaml

from pathlib import Path, PurePath
from functions import myplot

DEBUG = False

p = Path('{}/functions/my_logger.yaml'.format(PurePath(__file__).parent))
with p.open('r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

if DEBUG:
    logger = logging.getLogger('log_info')
else:
    logger = logging.getLogger('log_warning')

results_one, results_two = myplot.start_plot(user_param_file='projects_data/waterloo/user_parameters_elsewhere.yaml')

if DEBUG:
    logger.info('''
    results_one: {}
    results_two: {}
    '''.format(results_one, results_two))

# vim: ai et ts=4 sw=4 sts=4 nu ru
