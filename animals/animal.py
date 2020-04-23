class Animal:

    def __init__(self, species):
        self.species = species
        self.is_animal = True

    def feed(self, prey):
        print(f"{self.species} eats {prey}")