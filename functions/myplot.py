# -*- coding: utf-8 -*-
import logging, logging.config
import sys, yaml
from pathlib import Path, PurePath
import pandas as pd

DEBUG = True # Set to True for debugging information

p = Path('{}/my_logger.yaml'.format(PurePath(__file__).parent))
with p.open('r') as f:
    config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)

if DEBUG:
    logger = logging.getLogger('log_info')
else:
    logger = logging.getLogger('log_warning')

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


def log_up(up):
    """
    Used for logging, to examime the up object
    Split out as a function, so as not repeat myself
    """

    logger.info('''
        Let's examine this object:
        up.mountain_height: {} {}
        up.mountain_depth: {} {}
        up.data_file: {} {}
        up.image_directory: {} {}
        up.optional_parameter: {} {}
        '''.format(
        up.mountain_height, type(up.mountain_height),
        up.mountain_depth, type(up.mountain_depth),
        up.data_file, type(up.data_file),
        up.image_directory, type(up.image_directory),
        up.optional_parameter, type(up.optional_parameter),
        ))

def convert_yaml(p):
    """
    Takes yaml file, converts to dictionary, create up object
    """

    logger.info('yaml_file: {}'.format(p))
    up_prep = yaml.safe_load(p.open())
    logger.info('up_prep_dictionary: {}'.format(up_prep))
        
    up = UserParams(**up_prep)
    log_up(up)

    return up

def start_plot(user_param_file=None):
    """
    Get user parameters as up, and run myplot
    """
    
    if user_param_file == 'local':
        p = Path('{}/user_parameters.yaml'.format(PurePath(__file__).parent.parent))
        up = convert_yaml(p)
        
    elif user_param_file == 'sample':
        import functions.user_parameters as up
        log_up(up)

    else:
        try:
            p = Path('{}/{}'.format(
                           Path.home(),
                           user_param_file))
            up = convert_yaml(p)

        except Exception as e:

            logger.error('''Something is awry:
            {}
            '''.format(e))

            sys.exit('''
            Exiting ...
            ''')


    # Okay, up is now defined
    results_one, results_two = myplot(up=up)

    return results_one, results_two

def myplot(up=None):
    """
    Taking the user paramaeters, or sample parameters and do plots
    """

    if not up:
        logger.error('''
        Woa!
        The User parameters or sample parameters are missing!!
        Exiting ....
        ''')

        sys.exit()

    df = pd.read_csv(up.data_file, header=None)

    logger.info('''
    DataFrame.head(n=4): 
    {}
    '''.format(df.head(n=4)))

    logger.info('''
    DataFrame.shape: 
    {}
    '''.format(df.shape))

    logger.info('''
    DataFrame.dtypes: 
    {}
    '''.format(df.dtypes))

    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru
