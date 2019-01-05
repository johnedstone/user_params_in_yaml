# -*- coding: utf-8 -*-

'''
Remove: ~/zappa-git/zappa-webscrape/mw/heavy_lifting.py
'''

import logging, sys, yaml

DEBUG = True

if DEBUG:
    logging.basicConfig(format='%(levelname)s:%(filename)s:%(lineno)s:%(message)s', level=logging.INFO)

def start_plot(user_param=None):
    
    if user_param == 'local':
        user_params = yaml.safe_load(open('user_parameters.yaml'))

        logging.info('user_params: {}'.format(user_params))
        
    elif user_param == 'sample':
        pass
    else:
        try:
            with open('boo', 'r') as fh:
                data = fh.readlines

        except Exception as e:

            logging.error('''Something is awry:
            {}
            '''.format(e))

            sys.exit('''
            Exiting ...
            ''')

    results_one, results_two = myplot()

    return results_one, results_two

def myplot():


    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru
