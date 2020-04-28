from .environment import Environment
from interfaces import ISaltwater, Identifiable

class Coastline(Environment, Identifiable):

    def __init__(self, name="coastline", animal_capacity=15, plant_capacity=3, id=""):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self, id)
        self.image = '''
                   
        \ _ /
      -= (_) =-
        /   \         _\/_
          |           //o\  _\/_
   _____ _ __ __ ____ _ | __/o\\ _
 =-=-_-__=_-= _=_=-=_,-'|"'""-|-,_
  =- _=-=- -_=-=_,-"          |
    =- =- -=.--"
'''

    def add_inhabitant(self, item):
        if not item.likes_salt:
            raise TypeError(f"{item} can't live in this environment!")
        elif hasattr(item, "feed"):
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
