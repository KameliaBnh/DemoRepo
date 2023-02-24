import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

# Créer une fenêtre Tkinter
root = tk.Tk()

# Définir la taille maximale de l'image pour un écran de 13 pouces
max_width = 1366
max_height = 768

# Créer une fonction pour ouvrir un fichier ou un dossier
def open_file():
    # Filtrer les types de fichiers acceptables
    file_types = [('Fichiers images', '*.jpg;*.jpeg;*.png;*.gif'), ('Dossiers', '*')]
    
    # Ouvrir une boîte de dialogue pour sélectionner un fichier ou un dossier
    file_path = filedialog.askopenfilename(filetypes=file_types)

    # Afficher le fichier sélectionné
    if os.path.isdir(file_path):
        print('Vous avez sélectionné un dossier :', file_path)
    else:
        print('Vous avez sélectionné un fichier :', file_path)
        img = Image.open(file_path)
        
        # Redimensionner l'image si elle dépasse la taille maximale
        if img.width > max_width or img.height > max_height:
            ratio = min(max_width/img.width, max_height/img.height)
            img = img.resize((int(img.width*ratio), int(img.height*ratio)))
        
        photo = ImageTk.PhotoImage(img)
        label = tk.Label(root, image=photo)
        label.image = photo
        label.pack()

# Créer un bouton "Ouvrir"
open_button = tk.Button(root, text="Ouvrir", command=open_file)
open_button.pack()

# Afficher la fenêtre Tkinter
root.mainloop()
