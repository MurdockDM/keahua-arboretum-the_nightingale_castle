from .plant import Plant
from interfaces import Identifiable
from interfaces import ISunny

class Silversword(Plant, Identifiable, ISunny):

    def __init__(self, name = "Silversword", id=""):
        Plant.__init__(self, name)
        Identifiable.__init__(self, id="")
        ISunny.__init__(self)
        self.image = """
   _x_x__x_____x    
  x  / x | x x  \   
 x  x x| x |x x  x  
 |  | |x | || |  |  
 |  x || x x| |  x  
__\__x_x_|_x_x__/__ 
\                 / 
 `---------------'   
  |        :F_P:|     
  \_____________/
        """