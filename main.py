import sys
import os

# Ajoutez le dossier parent au chemin Python
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.zoo_view import ZooView
import tkinter as tk

if __name__ == "__main__":
    # Initialisation de la fenêtre principale Tkinter
    root = tk.Tk()

    # Création de l'interface ZooView
    app = ZooView(root)

    # Boucle principale Tkinter
    root.mainloop()
