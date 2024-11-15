class Cage:
    def __init__(self, id_cage):
        self.id_cage = id_cage
        self.animaux = []

    def ajouter_animal(self, animal):
        self.animaux.append(animal)

    def lister_animaux(self):
        if not self.animaux:
            return "La cage est vide."
        return "\n".join(str(animal) for animal in self.animaux)
