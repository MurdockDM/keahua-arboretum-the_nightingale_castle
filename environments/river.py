from .environment import Environment
from interfaces import IFreshwater, Identifiable

class River(Environment, Identifiable):

    def __init__(self, name="river", animal_capacity=12, plant_capacity=6, id=""):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self, id)
        self.image = '''
                                   _                  
                                  >')                 
               _   /              (\\         (W)     
              =') //               = \     -. `|'     
               ))////)             = ,-      \(| ,-   
              ( (///))           ( |/  _______\|/____ 
~~~~~~~~~~~~~~~`~~~~'~~~~~~~~~~~~~\|,-':::::::::::::: 
  ~~~     ~~      ~~~~    ~~  ,----'::::::::::::::::: 
~~       ~~~~~~~     ~~~ _.--'::::::::::::::::::::::: 
__,'`----._,-.  ~~~    _-'::::::::::::::::::::::::::: 
:.:.:.:.:.:.:.\_    ,-'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.: 
.:.:.:.:.:.:.:.:`--'.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:.:. 
'''

    def add_inhabitant(self, item):
        if not item.likes_freshwater:
            raise TypeError(f"{item} can't live in this environment!")
        elif hasattr(item, "feed"):
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name