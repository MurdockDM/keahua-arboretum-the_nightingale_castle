from .environment import Environment
from interfaces import ISunny, Identifiable

class Grassland(Environment, Identifiable):

    def __init__(self, name="grassland", animal_capacity=22, plant_capacity=15):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self)

    def add_inhabitant(self, item):
        if not item.likes_sun:
            raise TypeError(f"{item} can't live in this environment!")
        elif item.feed:
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
