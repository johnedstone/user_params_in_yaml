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

def simple_debug(up, df):
    """
    Leave here for debugging, i.e printing if not using IDE

    Feel free to delete this block of code
    """
    import logging
    logging.basicConfig(level=logging.INFO)

    logging.info("""
Here is up
    up.mountain_height and type: {} {} 
    up.mountain_depth and type: {} {}
    up.data_file and type: {} {}
    up.image_directory and type: {} {}
    up.title_for_graphing and type: {} {}

Here is df

df.head(n=4):
{}

df.shape: {}

df.size: {}

df.dtypes:
{}
    """.format(
        up.mountain_height, type(up.mountain_height),
        up.mountain_depth, type(up.mountain_depth),
        up.data_file, type(up.data_file),
        up.image_directory, type(up.image_directory),
        up.title_for_graphing, type(up.title_for_graphing),
        df.head(n=4),
        df.shape,
        df.size,
        df.dtypes,
        )
    )



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

    #simple_debug(up, df) # comment in/out for debugging

    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru

