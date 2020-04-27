from .environment import Environment
from interfaces import IShady, Identifiable

class Forest(Environment, Identifiable):

    def __init__(self, name="forest", animal_capacity=20, plant_capacity=32):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self)
        self.image = '''
               ,@@@@@@@,
       ,,,.   ,@@@@@@/@@,  .oo8888o.
    ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
   ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
   %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
   %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
   `&%\ ` /%&'    |.|        \ '|8'
       |o|        | |         | |
       |.|        | |         | |
    \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
'''

    def add_inhabitant(self, item):
        if not item.likes_shade:
            raise TypeError(f"{item} can't live in this environment!")
        elif item.feed:
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
