# -*- coding: utf-8 -*-
import  yaml
from pathlib import Path, PurePath
import pandas as pd

class UserParams():
    """
    Create object with user parameters as attributes
    """

    def __init__(self, **kwargs):
        self.mountain_height = kwargs['mountain_height']
        self.mountain_depth = kwargs['mountain_depth']
        self.data_file = str(Path('{}/{}'.format(
                                  Path.home(),
                                  kwargs['data_file'])))
        self.image_directory = str(Path('{}/{}'.format(
                                   Path.home(),
                                   kwargs['image_directory'])))
        self.title_for_graphing = kwargs['title_for_graphing']

        if 'optional_parameter' in kwargs:
            self.optional_parameter = kwargs['optional_parameter']
        else:
            self.optional_parameter = None


def start_plot(user_param_file=None):
    """
    Get user parameters as up, and run myplot
    """
    p = Path('{}/user_parameters.yaml'.format(PurePath(__file__).parent.parent))

    up_prep = yaml.safe_load(p.open())
        
    up = UserParams(**up_prep)
        
    results_one, results_two = myplot(up=up)

    return results_one, results_two


def myplot(up):
    """
    Taking the user paramaeters, or sample parameters and do plots
    """

    df = pd.read_csv(up.data_file, header=None)

    # Delete this block if no logging is needed
    from .barebones_logger import simple_debug
    simple_debug(up, df)

    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru
