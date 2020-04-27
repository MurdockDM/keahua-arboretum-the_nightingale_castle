from .environment import Environment
from interfaces import IHighElevation, Identifiable

class Mountain(Environment, Identifiable):

    def __init__(self, name="mountain", animal_capacity=6, plant_capacity=4):
        Environment.__init__(self, name, animal_capacity, plant_capacity)
        Identifiable.__init__(self)
        self.image = '''
                             
          /\               
         /**\              
        /****\   /\        
       /      \ /**\       
      /  /\    /    \      
     /  /  \  /      \     
    /  /    \/ /\     \    
   /  /      \/  \/\   \   
__/__/_______/___/__\___\  
'''

    def add_inhabitant(self, item):
        if not item.likes_high_elevation:
            raise TypeError(f"{item} can't live in this environment!")
        elif item.feed:
            self.inhabitants["Animals"].append(item)
        else:
            self.inhabitants["Plants"].append(item)

    def __str__(self):
        return self.name
