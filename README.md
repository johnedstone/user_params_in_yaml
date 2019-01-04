### Purpose
This repository has been created to demonstrate changing from the pattern of putting one's user_parameters in a Python file to the pattern of using a `user_parameters.yaml` file.

* The assumed project is called **Waterloo**
* This code should run on both Windows and Linux
* There is variable called DEBUG, related to printing and logging
* This project will demonstrate using print statments as well as Python's built-in logging.

#### Data and Code Directories: project_data/Waterloo and project_code/Waterloo
* Note that the data and the code directories are in separate places. That is, let's assume your data files and any output files are completely separated from your code directory.
* File paths are relative to one's Home Directory, using forward slashes (/) for both Windows and Linux
* Three options are provided:

    * run_me_my_vars_are_here.py: is for the case where one puts their custom vars in the code directory - common, but you may want to separate it and put it in your data directory.
    * run_me_my_vars_are_elsewhere.py is for the case where one puts their custom vars elsewhere, e.g. in one's project_data directory
    * run_me_sample_vars.py: is for running some sample vars, and this is the old way, demonstrating putting one's sample vars in a python file
