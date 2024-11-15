from components.zoo import Zoo
from components.cage import Cage
from components.animal import Carnivore, Herbivore, Omnivore, Frugivore
from components.visiteur import Visiteur





class ZooController:
    def __init__(self):
        self.zoo = Zoo("Mon Zoo")
        self.initialiser_donnees()

    def initialiser_donnees(self):
        """Initialise les données du zoo avec 50 visiteurs, des cages et des animaux."""
        # Ajouter des visiteurs initiaux
        self.zoo.nombre_visiteurs = 50
        self.zoo.chiffre_affaires = 50 * 5  # Chaque visiteur paie 5 euros
        
        # Ajouter des cages
        cage1 = Cage(1)
        cage2 = Cage(2)
        self.zoo.ajouter_cage(cage1)
        self.zoo.ajouter_cage(cage2)

        # Ajouter des animaux par défaut dans les cages
        lion = Carnivore("Roi", "Lion")
        gazelle = Herbivore("Gracieuse", "Gazelle")
        hyene = Carnivore("Rire", "Hyène")
        cage1.ajouter_animal(lion)
        cage1.ajouter_animal(hyene)
        cage2.ajouter_animal(gazelle)

    def ajouter_cage(self, cage_id):
        """Ajoute une nouvelle cage au zoo avec l'ID spécifié."""
        if any(c.id_cage == cage_id for c in self.zoo.cages):
            return False, f"La cage {cage_id} existe déjà."
        
        self.zoo.ajouter_cage(Cage(cage_id))
        return True, f"Cage {cage_id} ajoutée avec succès."

    def ajouter_animal(self, nom, espece, regime, cage_id):
        """Ajoute un animal dans une cage spécifiée par cage_id."""
        cage = next((c for c in self.zoo.cages if c.id_cage == cage_id), None)
        if not cage:
            return False, f"Aucune cage trouvée avec l'ID {cage_id}."

        # Gestion des différents régimes alimentaires
        regime = regime.lower()
        if regime == "carnivore":
            animal = Carnivore(nom, espece)
        elif regime == "herbivore":
            animal = Herbivore(nom, espece)
        elif regime == "omnivore":
            animal = Omnivore(nom, espece)
        elif regime == "frugivore":
            animal = Frugivore(nom, espece)
        else:
            return False, "Régime alimentaire invalide. Utilisez carnivore, herbivore, omnivore ou frugivore."

        cage.ajouter_animal(animal)
        return True, f"{nom} ({espece}) ajouté dans la cage {cage_id}."

    def ajouter_visiteurs(self, nombre_visiteurs):
        """Ajoute plusieurs visiteurs et augmente le chiffre d'affaires."""
        try:
            nombre_visiteurs = int(nombre_visiteurs)
            if nombre_visiteurs <= 0:
                return "Le nombre de visiteurs doit être un entier positif."
            self.zoo.ajouter_visiteurs(nombre_visiteurs)
            return f"{nombre_visiteurs} visiteurs ajoutés avec succès."
        except ValueError:
            return "Le nombre de visiteurs doit être un entier positif."

    def compter_visiteurs(self):
        """Renvoie le nombre total de visiteurs présents dans le zoo."""
        return self.zoo.compter_visiteurs()

    def get_chiffre_affaires(self):
        """Renvoie le chiffre d'affaires total généré par les visiteurs."""
        return self.zoo.get_chiffre_affaires()

    def lister_cages(self):
        """Renvoie une liste des cages et des animaux qu'elles contiennent."""
        return self.zoo.lister_cages()
