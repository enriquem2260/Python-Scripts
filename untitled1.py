# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:36:26 2023

@author: enriq
"""

import os

directory_path = "C:\\Users\\enriq\\OneDrive\\Documents\\Python\\UTSA"

# Check if the directory exists
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print(f"The directory '{directory_path}' did not exist and has been created.")

# You can now proceed to use the 'directory_path' as needed.

