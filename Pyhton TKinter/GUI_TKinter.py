import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk


# Define the function to open a file
def open_file():
    # Filter acceptable file types
    file_types = [('Image Files', '*.jpg;*.jpeg;*.png;*.gif')]

    # Open a dialog to select a file or folder
    file_path = filedialog.askopenfilename(filetypes=file_types)

    # Display the selected image
    img = Image.open(file_path)
    img.thumbnail((400, 600))
    photo = ImageTk.PhotoImage(img)
    image_label.configure(image=photo)
    image_label.image = photo

# Define the function to export the report
def export_report():
    print("Exporting report...")



# Create a Tkinter window
root = tk.Tk()
root.title("Automated Pollinator Monitoring")
root.geometry("800x600") # Set the size of the window

# Create a menu bar
menu_bar = tk.Menu(root)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="Export report", command=export_report)
root.config(menu=menu_bar)

# Create the frames
image_frame = tk.Frame(root, width=400, height=580, bd=1, relief="sunken")
options_frame = tk.Frame(root, width=380, height=280, bd= 1, relief="sunken")
statistics_frame = tk.Frame(root, width=380, height=300, bd= 1, relief="sunken")

# Create labels for each frame
image_label = tk.Label(image_frame)
options_label = tk.Label(options_frame, text="Options: ", padx=5, pady=5)
statistics_label = tk.Label(statistics_frame, text="Statistics: ", padx=5, pady=5)

# Place the labels at the top left corner of each frame
image_label.pack(side="top", anchor="nw")
options_label.pack(side="top", anchor="nw")
statistics_label.pack(side="top", anchor="nw")

# Place the frames on the window
image_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
options_frame.grid(row=0, column=1, padx=5, pady=5, sticky="n")
statistics_frame.grid(row=0, column=1, padx=5, pady=5, sticky="s")

# Make frames fixed in size
image_frame.pack_propagate(0)
options_frame.pack_propagate(0)
statistics_frame.pack_propagate(0)

# Display the Tkinter window
root.mainloop()
