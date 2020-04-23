from .animal import Animal
from interfaces import IFreshwater
from interfaces import ISaltwater
from .prey import FishFood
from interfaces import Identifiable

class RiverDolphin(Animal, IFreshwater, ISaltwater, Identifiable, FishFood):

    def __init__(self, name):
        Animal.__init__(self, name)
        IFreshwater.__init__(self)
        ISaltwater.__init__(self)
        FishFood.__init__(self)
        Identifiable.__init__(self)

    def feed(self, prey):
        print(f"{self.species} eats {prey}")    

    def __str__(self):
        return f'Dolphin {self.id}. Eeee EeeEEeeeeEE!'
