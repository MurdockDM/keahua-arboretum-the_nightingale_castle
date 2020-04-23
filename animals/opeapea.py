from .animal import Animal
from interfaces import IShady
from interfaces import IHighElevation
from .prey import VegetationFood
from .prey import InsectFood
from interfaces import Identifiable

class Opeapea(Animal, IShady, IHighElevation, VegetationFood, Identifiable):

    def __init__(self, name):
        Animal.__init__(self, name)
        VegetationFood.__init__(self)
        IShady.__init__(self)
        IHighElevation.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    

    def __str__(self):
        return f"Opeapea {self.id}. Squeak"
