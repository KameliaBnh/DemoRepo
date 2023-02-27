import tkinter as tk
from PIL import Image, ImageTk


# Define the function to open a file
def open_file():
    # Filter acceptable file types
    file_types = [('Image Files', '*.jpg;*.jpeg;*.png;*.gif')]

    # Open a dialog to select a file or folder
    file_path = tk.filedialog.askopenfilename(filetypes=file_types)

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
root.iconbitmap('C:/Users/benha/Documents/Cranfield/Group Project/Test Different GUI/Pyhton TKinter/bee.ico')
root.geometry("800x620") # Set the size of the window

# Create a menu bar
menu_bar = tk.Menu(root)
menu_bar.add_command(label="Open", command=open_file)
menu_bar.add_command(label="Export report", command=export_report)
root.config(menu=menu_bar)

# Create the frames
image_frame = tk.LabelFrame(root, width=400, height=580, bd=1, relief="sunken", text="Visualisation: ")
options_frame = tk.LabelFrame(root, width=370, height=220, bd= 1, relief="sunken", text="Options: ")
statistics_frame = tk.LabelFrame(root, width=370, height=350, bd= 1, relief="sunken", text="Statistics: ")

# Create label to display image
image_label = tk.Label(image_frame)
image_label.pack(side="top", anchor="nw")

# Place the frames on the window
image_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
options_frame.grid(row=0, column=1, padx=5, pady=5, sticky="n")
statistics_frame.grid(row=0, column=1, padx=5, pady=5, sticky="s")

# Make frames fixed in size
image_frame.pack_propagate(0)
options_frame.pack_propagate(0)
statistics_frame.pack_propagate(0)


## OPTIONS PANE ##

# Create options for the detection model
MODELS = [
    ("Yolov5", "Yolov5"),
    ("Yolov8", "Yolov8")
]

model=tk.StringVar()
model.set("Yolov5")

model_label = tk.Label(options_frame, text="Model: ", padx=5, pady=10)
model_label.pack(side="top", anchor="nw")

for model_name, model_value in MODELS:
    tk.Radiobutton(options_frame, text=model_name, padx=5, pady=5, variable=model, value=model_value).pack(side="top")

videoTrack = tk.StringVar()
videoTrack.set("No")

trackButton = tk.Checkbutton(options_frame, text="Tracking Video", variable=videoTrack, onvalue="Yes", offvalue="No")
trackButton.pack()

def start_classification():
    start_label = tk.Label(options_frame, text="Classification model for " + str((model.get())) + " started", padx=5, pady=5) #model.get() returns the value of the selected radio button
    start_label.pack(side="bottom", padx=5, pady=5)

# Create start button for the detection model
start_button = tk.Button(options_frame, text="Start", command=start_classification, padx=5, pady=5)
start_button.pack(side="bottom", padx=5, pady=5)


############################################################################################################################################################################


## STATISTICS PANE ##

species_label = tk.Label(statistics_frame, text="Species name: ", padx=5, pady=10)
species_label.pack(side="top", anchor="nw")

species_label = tk.Label(statistics_frame, text="Species info: ", padx=5, pady=5)
species_label.pack(side="top", anchor="nw")

############################################################################################################################################################################



# Display the Tkinter window
root.mainloop()
