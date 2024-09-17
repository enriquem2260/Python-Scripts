# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:39:07 2023

@author: enriq
"""

import os

# Specify the file or directory path
path_to_check = "C:\\Users\\enriq\\OneDrive\\Documents\\Python\\UTSA"

# Check if it's a directory
if os.path.isdir(path_to_check):
    print(f"The path '{path_to_check}' is a directory.")
elif os.path.isfile(path_to_check):
    print(f"The path '{path_to_check}' is a file.")
else:
    print(f"The path '{path_to_check}' does not exist.")
