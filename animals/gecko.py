from .animal import Animal
from interfaces import IShady
from .prey import InsectFood
from interfaces import Identifiable

class Gecko(Animal, IShady, InsectFood, Identifiable):

    def __init__(self, name):
        Animal.__init__(self, name)
        IShady.__init__(self)
        InsectFood.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    
    

    def __str__(self):
        return f"Gecko {self.id}. Slurp Slurp"