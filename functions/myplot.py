# -*- coding: utf-8 -*-
import logging, sys, yaml

DEBUG = True

with open('functions/my_logger.yaml', 'r') as f:
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
        self.data_file = kwargs['data_file']
        self.image_directory = kwargs['image_directory']
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

def start_plot(user_param=None):
    """
    Get user parameters as up, and run myplot
    """
    
    if user_param == 'local':
        # turn yaml into a dictionary
        up_prep = yaml.safe_load(open('user_parameters.yaml'))

        logger.info('up_prep: {}'.format(up_prep))
        
        up = UserParams(**up_prep) # This passes the use_params dictionary to creating the object

        _ = log_up(up)
        
    elif user_param == 'sample':
        import functions.user_parameters as up
        _ = log_up(up)

    else:
        try:
            with open('boo', 'r') as fh:
                data = fh.readlines

        except Exception as e:

            logger.error('''Something is awry:
            {}
            '''.format(e))

            sys.exit('''
            Exiting ...
            ''')


    # Okay, up is now defined
    results_one, results_two = myplot()

    return results_one, results_two

def myplot():


    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru
