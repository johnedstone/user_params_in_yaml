# -*- coding: utf-8 -*-
"""
This file will use the file functions/user_parameters.py which may have been how you started
"""

import logging
import logging.config
import yaml

from pathlib import Path, PurePath
from functions import myplot

DEBUG = False

logger_path = Path('{}/functions/my_logger.yaml'.format(PurePath(__file__).parent))
with open(str(logger_path), 'r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

if DEBUG:
    logger = logging.getLogger('log_info')
else:
    logger = logging.getLogger('log_warning')

results_one, results_two = myplot.start_plot(user_param_file='sample')

logger.info('''
    results_one: {}
    results_two: {}
    '''.format(results_one, results_two))

# vim: ai et ts=4 sw=4 sts=4 nu ru
