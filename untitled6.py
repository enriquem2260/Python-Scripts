# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:23:03 2023

@author: enriq
"""

from getpass import getpass
 
class GraphicalPasswordAuthenticator:
    """
    Class to authenticate users using a graphical password.
 
    Attributes:
    - password: str
        The graphical password set by the user during registration.
    """
 
    def __init__(self, password: str):
        """
        Constructor to instantiate the GraphicalPasswordAuthenticator class.
 
        Parameters:
        - password: str
            The graphical password set by the user during registration.
        """
 
        self.password = password
 
    def authenticate_user(self):
        """
        Authenticates the user by comparing the entered graphical password with the stored password.
 
        Returns:
        - bool:
            True if the entered password matches the stored password, False otherwise.
        """
 
        # Prompting the user to enter the graphical password
        entered_password = getpass("Enter your graphical password: ")
 
        # Comparing the entered password with the stored password
        if entered_password == self.password:
            return True
        else:
            return False
 
# Example usage of the GraphicalPasswordAuthenticator class:
 
# Example 1: Authenticating the user
registered_password = "password123"  # Assume this is the password set during registration
authenticator = GraphicalPasswordAuthenticator(registered_password)
is_authenticated = authenticator.authenticate_user()
 
if is_authenticated:
    print("User authenticated successfully!")
else:
    print("Authentication failed!")