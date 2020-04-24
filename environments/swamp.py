import sys
sys.path.append('../')

from .environment import Environment
from interfaces.habitat import IStagnant

class Swamp(Environment):

    def __init__(self, name="swamp", animal_capacity=8, plant_capacity=12):
        super().__init__(name, animal_capacity, plant_capacity)

    def add_inhabitant(self, item):
        if not isinstance(item, IStagnant):
            raise TypeError(f"{item} can't live in this environment!")
        elif item.is_animal:
            self.inhabitants["Animals"].append(item)
        elif item.is_plant:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
