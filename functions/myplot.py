# -*- coding: utf-8 -*-

'''
Remove: ~/zappa-git/zappa-webscrape/mw/heavy_lifting.py
'''

import sys, yaml

DEBUG = True

def start_plot(user_param=None):
    
    if user_param == 'local':
        user_params = yaml.load(open('user_parameters.yaml'))

        if DEBUG:
            print('user_params: {}'.format(user_params))
        
    elif user_param == 'sample':
        pass
    else:
        try:
            pass
        except Exception as e:

            print('Something is awry: {}'.format(e))
            sys.exit('''
            Exiting ...
            ''')

    results_one, results_two = myplot()

    return results_one, results_two

def myplot():


    return 'boo', 'hoo'

# vim: ai et ts=4 sw=4 sts=4 nu ru
