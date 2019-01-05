### Purpose
This repository has been created to demonstrate changing from the pattern of putting the user parameters in a Python file to the pattern of using a `user_parameters.yaml` file.

* The assumed project is called **Waterloo**
* This code should run on both Windows and Linux
* There is variable called DEBUG (True or False) related to logging.
* Reference for python logging

    * https://docs.python.org/3/howto/logging.html#logging-basic-tutorial
    * https://docs.python.org/3/howto/logging.html#loggers 

#### Data and Code Directories: project_data/Waterloo and project_code/Waterloo
* Note that the data and the code directories are in separate places.

    * That is, let's assume your data files and any output files are completely separated from your code directory.

* File paths are relative to one's Home Directory, using forward slashes (/) for both Windows and Linux
* Three options are provided:

    * run_me_my_params_are_here.py: is for the case where one puts their custom params in the code directory. This is a common practice, but you may want to put it in your project data directory.
    * run_me_my_params_are_elsewhere.py is for the case where one puts their custom params elsewhere, e.g. in one's project_data directory
    * run_me_sample_params.py: is for running some sample params, and this is the old way, demonstrating putting one's sample params in a python file
