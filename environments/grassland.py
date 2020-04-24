from .environment import Environment
from interfaces import ISunny

class Grassland(Environment):

    def __init__(self, name="grassland", animal_capacity=22, plant_capacity=15):
        super().__init__(name, animal_capacity, plant_capacity)

    def add_inhabitant(self, item):
        if not isinstance(item, ISunny):
            raise TypeError(f"{item} can't live in this environment!")
        elif item.is_animal:
            self.inhabitants["Animals"].append(item)
        elif item.is_plant:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
