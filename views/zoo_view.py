import tkinter as tk
from tkinter import messagebox
from controllers.zoo_controller import ZooController
from PIL import Image, ImageTk

class ZooView:
    def __init__(self, root):
        self.controller = ZooController()
        self.root = root
        self.root.title("Gestion du Zoo")
        
        # Définir la taille de la fenêtre
        self.root.geometry("1500x1500")

        # Charger l'image de fond
        self.background_image = Image.open("img/35637.jpg")
        self.background_image = self.background_image.resize((1500, 1500), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Créer un Canvas pour afficher l'image de fond
        self.canvas = tk.Canvas(root, width=1500, height=1500)
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")

        # Titre principal
        self.canvas.create_text(750, 30, text="Gestion du Zoo", font=("Arial", 24), fill="white")

        # === Section pour ajouter une cage ===
        self.canvas.create_text(150, 100, text="Ajouter une Cage", font=("Arial", 18), fill="white")
        self.canvas.create_text(100, 150, text="ID de la Cage :", font=("Arial", 14), fill="white")
        self.cage_id_entry = tk.Entry(root)
        self.canvas.create_window(250, 150, window=self.cage_id_entry)
        
        ajouter_cage_button = tk.Button(root, text="Ajouter Cage", command=self.ajouter_cage)
        self.canvas.create_window(400, 150, window=ajouter_cage_button)

        # === Section pour ajouter un animal ===
        self.canvas.create_text(150, 200, text="Ajouter un Animal", font=("Arial", 18), fill="white")
        self.canvas.create_text(100, 250, text="Nom de l'Animal :", font=("Arial", 14), fill="white")
        self.animal_nom_entry = tk.Entry(root)
        self.canvas.create_window(250, 250, window=self.animal_nom_entry)

        self.canvas.create_text(100, 300, text="Espèce :", font=("Arial", 14), fill="white")
        self.animal_espece_entry = tk.Entry(root)
        self.canvas.create_window(250, 300, window=self.animal_espece_entry)

        self.canvas.create_text(100, 350, text="Régime (carnivore/herbivore/omnivore/frugivore) :", font=("Arial", 14), fill="white")
        self.animal_regime_entry = tk.Entry(root)
        self.canvas.create_window(350, 350, window=self.animal_regime_entry)

        self.canvas.create_text(100, 400, text="ID de la Cage :", font=("Arial", 14), fill="white")
        self.animal_cage_id_entry = tk.Entry(root)
        self.canvas.create_window(250, 400, window=self.animal_cage_id_entry)

        ajouter_animal_button = tk.Button(root, text="Ajouter Animal", command=self.ajouter_animal)
        self.canvas.create_window(400, 400, window=ajouter_animal_button)

        # === Section pour ajouter des visiteurs ===
        self.canvas.create_text(150, 450, text="Ajouter des Visiteurs", font=("Arial", 18), fill="white")
        self.canvas.create_text(100, 500, text="Nombre de Visiteurs :", font=("Arial", 14), fill="white")
        self.visiteurs_nombre_entry = tk.Entry(root)
        self.canvas.create_window(250, 500, window=self.visiteurs_nombre_entry)

        ajouter_visiteurs_button = tk.Button(root, text="Ajouter Visiteurs", command=self.ajouter_visiteurs)
        self.canvas.create_window(400, 500, window=ajouter_visiteurs_button)

        # === Boutons pour afficher les informations ===
        nombre_visiteurs_button = tk.Button(root, text="Nombre de Visiteurs", command=self.afficher_nombre_visiteurs)
        self.canvas.create_window(250, 550, window=nombre_visiteurs_button)

        chiffre_affaires_button = tk.Button(root, text="Chiffre d'Affaires", command=self.afficher_chiffre_affaires)
        self.canvas.create_window(400, 550, window=chiffre_affaires_button)

        lister_cages_button = tk.Button(root, text="Lister les Cages", command=self.afficher_cages)
        self.canvas.create_window(250, 600, window=lister_cages_button)

    def ajouter_cage(self):
        cage_id = self.cage_id_entry.get()
        if not cage_id.isdigit():
            messagebox.showerror("Erreur", "L'ID de la cage doit être un chiffre.")
            return
        cage_id = int(cage_id)
        success, message = self.controller.ajouter_cage(cage_id)
        if success:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def ajouter_animal(self):
        nom = self.animal_nom_entry.get()
        espece = self.animal_espece_entry.get()
        regime = self.animal_regime_entry.get()
        cage_id = self.animal_cage_id_entry.get()

        if not cage_id.isdigit():
            messagebox.showerror("Erreur", "L'ID de la cage doit être un chiffre.")
            return

        cage_id = int(cage_id)
        success, message = self.controller.ajouter_animal(nom, espece, regime, cage_id)
        if success:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def ajouter_visiteurs(self):
        nombre_visiteurs = self.visiteurs_nombre_entry.get()
        if not nombre_visiteurs.isdigit() or int(nombre_visiteurs) <= 0:
            messagebox.showerror("Erreur", "Veuillez entrer un nombre entier positif pour les visiteurs.")
            return

        nombre_visiteurs = int(nombre_visiteurs)
        message = self.controller.ajouter_visiteurs(nombre_visiteurs)
        if "succès" in message:
            messagebox.showinfo("Succès", message)
        else:
            messagebox.showerror("Erreur", message)

    def afficher_nombre_visiteurs(self):
        nombre_visiteurs = self.controller.compter_visiteurs()
        messagebox.showinfo("Nombre de Visiteurs", f"Nombre total de visiteurs : {nombre_visiteurs}")

    def afficher_chiffre_affaires(self):
        chiffre_affaires = self.controller.get_chiffre_affaires()
        messagebox.showinfo("Chiffre d'Affaires", f"Chiffre d'affaires du jour : {chiffre_affaires} €")

    def afficher_cages(self):
        cages_info = self.controller.lister_cages()
        messagebox.showinfo("Liste des Cages", cages_info)


# Lancer l'interface
if __name__ == "__main__":
    root = tk.Tk()
    app = ZooView(root)
    root.mainloop()
