from .environment import Environment
from interfaces import IShady

class Forest(Environment):

    def __init__(self, name, animal_capacity, plant_capacity):
        super().__init__(name, animal_capacity, plant_capacity)

    def add_inhabitant(self, item):
        if not isinstance(item, IShady):
            raise TypeError(f"{item} can't live in this environment!")
        elif item.is_animal:
            self.inhabitants["Animals"].append(item)
        elif item.is_plant:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
