# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 22:25:52 2023

@author: enriq
"""

from tkinter import Tk
from tkinter import messagebox
from PIL import Image, ImageTk
from getpass import getpass

class GraphicalPasswordAuthenticator:
    # (rest of the class remains the same)

    def create_password_prompt(self):
        # Create a Tkinter window for the graphical password prompt
        root = Tk()
        root.title("Graphical Password Authenticator")

        # Load and display the image as a prompt
        image_path = "path_to_your_image.png"  # Replace with the path to your image
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        img_label = Label(root, image=img)
        img_label.pack()

        # Example usage of the GraphicalPasswordAuthenticator class:

        # ... (rest of the code remains the same)

        # Prompt the user to enter the graphical password
        entered_password = getpass("Enter your graphical password: ")

        # Close the Tkinter window after getting the password
        root.destroy()

        # Authenticating the user
        if self.authenticate_user(entered_password):
            print("User authenticated successfully!")
        else:
            print("Authentication failed!")

# Create an instance of the GraphicalPasswordAuthenticator class
authenticator = GraphicalPasswordAuthenticator()

# Call the method to create the password prompt and authenticate the user
authenticator.create_password_prompt()
