import sys
sys.path.append('../')

from .environment import Environment
from interfaces import IStagnant, Identifiable

class Swamp(Environment, Identifiable):

    def __init__(self, name="swamp", animal_capacity=8, plant_capacity=12):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self)

    def add_inhabitant(self, item):
        if not item.likes_stagnant_water:
            raise TypeError(f"{item} can't live in this environment!")
        elif item.feed:
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
