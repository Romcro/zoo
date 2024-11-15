from .cage import Cage
from .visiteur import Visiteur

class Zoo:
    def __init__(self, nom):
        self.nom = nom
        self.cages = []
        self.visiteurs = []
        self.nombre_visiteurs = 50  # Commence avec 50 visiteurs
        self.chiffre_affaires = 50 * 5  # 5 € par visiteur

    def ajouter_visiteurs(self, nombre_visiteurs):
        """Ajoute plusieurs visiteurs au zoo."""
        if not isinstance(nombre_visiteurs, int) or nombre_visiteurs <= 0:
            raise ValueError("Le nombre de visiteurs doit être un entier positif.")
        self.nombre_visiteurs += nombre_visiteurs
        self.chiffre_affaires += nombre_visiteurs * 5  # Chaque visiteur paie 5 euros

    def ajouter_cage(self, cage):
        self.cages.append(cage)

    def compter_visiteurs(self):
        return self.nombre_visiteurs

    def get_chiffre_affaires(self):
        return self.chiffre_affaires

    def lister_cages(self):
        if not self.cages:
            return "Aucune cage n'est présente dans le zoo."
        
        cages_info = ""
        for cage in self.cages:
            cages_info += f"Cage {cage.id_cage} : {len(cage.animaux)} animal(aux)\n"
            cages_info += "  Animaux :\n"
            cages_info += "\n".join(f"    - {animal}" for animal in cage.animaux) + "\n"
        return cages_info
