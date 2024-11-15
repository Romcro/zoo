class Animal:
    def __init__(self, nom, espece, regime):
        self.nom = nom
        self.espece = espece
        self.regime = regime

    def __str__(self):
        return f"{self.espece} - {self.nom}"


class Carnivore(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece, "carnivore")


class Herbivore(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece, "herbivore")


class Omnivore(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece, "omnivore")

class Frugivore(Animal):
    def __init__(self, nom, espece):
        super().__init__(nom, espece, regime="frugivore")

    def __str__(self):
        return f"{self.nom} ({self.espece}, {self.regime})"
