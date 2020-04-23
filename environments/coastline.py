from .environment import Environment
from interfaces import ISaltwater

class Coastline(Environment):

    def __init__(self, name, animal_capacity, plant_capacity):
        super().__init__(name, animal_capacity, plant_capacity)

    def add_inhabitant(self, item):
        if not isinstance(item, ISaltwater):
            raise TypeError(f"{item} can't live in this environment!")
        elif item.is_animal:
            self.inhabitants["Animal"].append(item)
        elif item.is_plant:
            self.inhabitants["Plant"].append(item)

    def __str__(self):
        return self.name
