import customtkinter as ctk

ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

app = ctk.CTk()
app.geometry("800x620")
app.grid_rowconfigure(0, weight=1)  # configure grid system
app.grid_columnconfigure(0, weight=1)
app.title("Automated Pollinator Monitoring")
app.iconbitmap('C:/Users/benha/Documents/Cranfield/Group Project/Test Different GUI/Pyhton TKinter/bee.ico')

# Create frames

image_frame = ctk.CTkFrame(master=app, width=400, height=560)
image_frame.grid(padx=5, pady=5, rowspan=2, column=0, sticky="nsew")

options_frame = ctk.CTkFrame(master=app, width=370, height=220)
options_frame.grid(padx=5, pady=5, row=0, column=1, sticky="nsew")

stats_frame = ctk.CTkFrame(master=app, width=370, height=340)
stats_frame.grid(padx=5, pady=5, row=1, column=1, sticky="nsew")

# Populate frames

label_1 = ctk.CTkLabel(master=image_frame, justify=ctk.LEFT)
label_1.pack(pady=10, padx=10)

progressbar_1 = ctk.CTkProgressBar(master=image_frame)
progressbar_1.pack(pady=10, padx=10)

button_1 = ctk.CTkButton(master=image_frame)
button_1.pack(pady=10, padx=10)

slider_1 = ctk.CTkSlider(master=image_frame, from_=0, to=1)
slider_1.pack(pady=10, padx=10)
slider_1.set(0.5)

entry_1 = ctk.CTkEntry(master=image_frame, placeholder_text="CTkEntry")
entry_1.pack(pady=10, padx=10)

optionmenu_1 = ctk.CTkOptionMenu(image_frame, values=["Option 1", "Option 2", "Option 42 long long long..."])
optionmenu_1.pack(pady=10, padx=10)
optionmenu_1.set("CTkOptionMenu")

combobox_1 = ctk.CTkComboBox(image_frame, values=["Option 1", "Option 2", "Option 42 long long long..."])
combobox_1.pack(pady=10, padx=10)
combobox_1.set("CTkComboBox")

checkbox_1 = ctk.CTkCheckBox(master=image_frame)
checkbox_1.pack(pady=10, padx=10)

radiobutton_var = ctk.IntVar(value=1)

radiobutton_1 = ctk.CTkRadioButton(master=image_frame, variable=radiobutton_var, value=1)
radiobutton_1.pack(pady=10, padx=10)

radiobutton_2 = ctk.CTkRadioButton(master=image_frame, variable=radiobutton_var, value=2)
radiobutton_2.pack(pady=10, padx=10)

switch_1 = ctk.CTkSwitch(master=image_frame)
switch_1.pack(pady=10, padx=10)

text_1 = ctk.CTkTextbox(master=image_frame, width=200, height=70)
text_1.pack(pady=10, padx=10)
text_1.insert("0.0", "CTkTextbox\n\n\n\n")

segmented_button_1 = ctk.CTkSegmentedButton(master=image_frame, values=["CTkSegmentedButton", "Value 2"])
segmented_button_1.pack(pady=10, padx=10)

tabview_1 = ctk.CTkTabview(master=image_frame, width=200, height=70)
tabview_1.pack(pady=10, padx=10)
tabview_1.add("CTkTabview")
tabview_1.add("Tab 2")

app.mainloop()