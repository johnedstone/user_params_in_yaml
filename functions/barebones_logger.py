# -*- coding: utf-8 -*-
import logging
logging.basicConfig(level=logging.INFO)

def simple_debug(up, df):
    """
    Leave here for debugging, i.e printing if not using IDE

    Feel free to delete this block of code
    """

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

    return

# vim: ai et ts=4 sw=4 sts=4 nu ru
