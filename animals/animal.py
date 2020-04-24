class Animal:

    def __init__(self, species):
        self.species = species

    def feed(self, prey):
        print(f"{self.species} eats {prey}")