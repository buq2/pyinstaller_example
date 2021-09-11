#!/usr/bin/env python3
import os
import sys

def add_to_path(p):
    os.environ['PATH'] = p + os.pathsep + os.environ['PATH']

def get_script_location():
    if getattr(sys, 'frozen', False) and hasattr(sys, '_MEIPASS'):
        # Running from PyInstaller
        # Return location of the extracted package
        location = os.path.realpath(sys._MEIPASS)
    else:
        # Normal python run
        # When running PyInstaller package this would incorrectly return
        # current working directory
        location = os.path.dirname(os.path.realpath(__file__))
    print('Script location', location)
    return location

add_to_path(get_script_location())

import tool
tool.main()
