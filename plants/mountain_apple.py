from .plant import Plant
from interfaces import Identifiable
from interfaces import IHighElevation

class MountainApple(Plant, Identifiable, IHighElevation):

    def __init__(self, name = "Mountain Apple", id=""):
        Plant.__init__(self, name)
        Identifiable.__init__(self, id)
        IHighElevation.__init__(self)
        self.image = """ 
                                  _/`.-'`.
                _      _/` .  _.'
       ..:::::.(_)   /` _.'_./
     .oooooooooo\ \o/.-'__.'o.
    .ooooooooo`._\_|_.'`oooooob.
  .ooooooooooooooooooooo&&oooooob.
 .oooooooooooooooooooo&@@@@@@oooob.
.ooooooooooooooooooooooo&&@@@@@ooob.
doooooooooooooooooooooooooo&@@@@ooob
doooooooooooooooooooooooooo&@@@oooob
dooooooooooooooooooooooooo&@@@ooooob
dooooooooooooooooooooooooo&@@oooooob
`dooooooooooooooooooooooooo&@ooooob'
 `doooooooooooooooooooooooooooooob'
  `doooooooooooooooooooooooooooob'
   `doooooooooooooooooooooooooob'
    `doooooooooooooooooooooooob'
     `doooooooooooooooooooooob'
      `dooooooooobodoooooooob'
       `doooooooob dooooooob'
        """