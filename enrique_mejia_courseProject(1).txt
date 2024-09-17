# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Define a list of image filenames for users to choose from
image_filenames = [r"C:\Users\enriq\OneDrive\Pictures\UTSA\image1.png", r"C:\Users\enriq\OneDrive\Pictures\UTSA\image2.png", r"C:\Users\enriq\OneDrive\Pictures\UTSA\image3.png", r"C:\Users\enriq\OneDrive\Pictures\UTSA\image4.png"]

# Declare global variables
photo_images = []

for image_filename in image_filenames:
    image = tk.PhotoImage(file=image_filename)
    photo_images.append(image)
    
images_buttons = {}

# Global variable to store the user's selected images
selected_images = []

def image_clicked(image_filename):
    if image_filename in selected_images:
        selected_images.remove(image_filename)
        images_buttons[image_filename].config(relief="raised")
    else:
        selected_images.append(image_filename)
        images_buttons[image_filename].config(relief="sunken")

def verify_password():
    # Replace this with your own password validation logic
    correct_password = ["image1.png", "image2.png", "image3.png"]
    if selected_images == correct_password:
        messagebox.showinfo("Success", "Password Correct. Access Granted!")
    else:
        messagebox.showerror("Error", "Password Incorrect. Access Denied.")
    selected_images.clear()
    for image_filename in image_filenames:
        images_buttons[image_filename].config(relief="raised")

# Function to display selected images
def display_images():
    # Create a Tkinter window for displaying images
    display_window = tk.Tk()
    display_window.title("Selected Images")

    for image_filename in selected_images:
        # Open the image using Pillow (PIL)
        image = Image.open(image_filename)

        # Create a PhotoImage object from the PIL image
        photo = ImageTk.PhotoImage(image)

        # Create a Label widget to display the image
        label = tk.Label(display_window, image=photo)
        label.image = photo  # Keep a reference to the image
        label.pack()

    display_window.mainloop()

# Create the main window
root = tk.Tk()
root.title("Graphical Password Authenticator")

# Create a list to store PhotoImage objects
photo_images = []

for image_filename in image_filenames:
    image = tk.PhotoImage(file=image_filename)
    photo_images.append(image)

# Create buttons for image selection
images_buttons = {}
for image_filename in image_filenames:
    image_button = tk.Button(root, image=tk.PhotoImage(file=image_filename), command=lambda img=image_filename: image_clicked(img))
    image_button.grid(row=0, column=image_filenames.index(image_filename))
    images_buttons[image_filename] = image_button

# Create a verify button
verify_button = tk.Button(root, text="Verify Password", command=verify_password)
verify_button.grid(row=1, columnspan=len(image_filenames))

# Create a display button
display_button = tk.Button(root, text="Display Selected Images", command=display_images)
display_button.grid(row=2, columnspan=len(image_filenames))

# Start the Tkinter main loop
root.mainloop()
