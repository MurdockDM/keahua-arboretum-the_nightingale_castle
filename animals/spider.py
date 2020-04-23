from .animal import Animal
from interfaces import IStagnant
from .prey import InsectFood
from interfaces import Identifiable

class Spider(Animal, IStagnant, InsectFood, Identifiable):

    def __init__(self, name):
        Animal.__init__(self, name)
        InsectFood.__init__(self)
        IStagnant.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")

    def __str__(self):
        return f"Spider {self.id}. Quietly plots"