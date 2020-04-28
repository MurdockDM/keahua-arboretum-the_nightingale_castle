from .animal import Animal
from interfaces import ISunny
from interfaces import IShady
from .prey import RodentFood
from interfaces import Identifiable

class Pueo(Animal, ISunny, IShady, RodentFood, Identifiable):

    def __init__(self, name = "Pueo", id=""):
        Animal.__init__(self, name)
        RodentFood.__init__(self)
        ISunny.__init__(self)
        IShady.__init__(self)
        Identifiable.__init__(self, id)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    

    def __str__(self):
        return f"Pueo {self.id} Hoo Hoo"