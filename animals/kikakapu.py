from .animal import Animal
from interfaces import IStagnant
from interfaces import IFreshwater
from .prey import FishFood
from interfaces import Identifiable

class Kikakapu(Animal, IStagnant, IFreshwater, FishFood, Identifiable):

    def __init__(self, name = "Kīkākapu"):
        Animal.__init__(self, name)
        FishFood.__init__(self)
        IStagnant.__init__(self)
        IFreshwater.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    

    def __str__(self):
        return f"Kikakapu {self.id}. Blurp Blurp"