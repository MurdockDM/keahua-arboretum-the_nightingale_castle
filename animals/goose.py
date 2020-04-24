from .animal import Animal
from interfaces import ISunny
from .prey import VegetationFood
from interfaces import Identifiable

class Goose(Animal, ISunny, VegetationFood, Identifiable):

    def __init__(self, name = "Nene Goose"):
        Animal.__init__(self, name)
        VegetationFood.__init__(self)
        ISunny.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    

    def __str__(self):
        return f"Goose {self.id}. Honk Honk"