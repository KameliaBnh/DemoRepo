import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Create a Tkinter window
root = tk.Tk()

# Define the maximum size of the image for a 13-inch screen
max_width = 1366
max_height = 768

# Create a function to open a file or a folder
def open_file():
    # Filter acceptable file types
    file_types = [('Image files', '*.jpg;*.jpeg;*.png;*.gif'), ('Folders', '*')]
    
    # Open a dialog box to select a file or folder
    file_path = filedialog.askopenfilename(filetypes=file_types)

    # Display the selected file
    if os.path.isdir(file_path):
        print('You selected a folder:', file_path)
    else:
        print('You selected a file:', file_path)
        img = Image.open(file_path)
        
        # Resize the image if it exceeds the maximum size
        if img.width > max_width or img.height > max_height:
            ratio = min(max_width/img.width, max_height/img.height)
            img = img.resize((int(img.width*ratio), int(img.height*ratio)))
        
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()

# Create an "Open" button
open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack()

# Display the Tkinter window
root.mainloop()

# Now you have your graphical user interface!
