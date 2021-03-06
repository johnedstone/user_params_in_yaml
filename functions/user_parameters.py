# -*- coding: utf-8 -*-
"""
This could be some sample data,
or perhaps this is how you started,
putting user input in a python file
"""

from pathlib import Path

mountain_height = 205.65
mountain_depth = 22
data_file = Path('{}/{}'.format(
    Path.home(),
    'projects_data/waterloo/data/waterloo_data.csv'))
image_directory = 'projects_data/waterloo/images'
title_for_graphing = 'Waterloo 2019'
optional_parameter = 107.10

# vim: ai et ts=4 sw=4 sts=4 nu ru
