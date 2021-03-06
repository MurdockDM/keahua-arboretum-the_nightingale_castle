from .animal import Animal
from interfaces import ISaltwater
from .prey import FishFood
from interfaces import Identifiable

class Ulae(Animal, ISaltwater, FishFood, Identifiable):

    def __init__(self, name = "'Ulae"):
        Animal.__init__(self, name)
        FishFood.__init__(self)
        ISaltwater.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")

    def __str__(self):
        return f"Ulae {self.id}. Blurp Blurp"