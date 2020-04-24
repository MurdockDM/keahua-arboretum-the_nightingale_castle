from .plant import Plant
from interfaces import Identifiable
from interfaces import IHighElevation

class MountainApple(Plant, Identifiable, IHighElevation):

    def __init__(self, name = "Mountain Apple"):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        IHighElevation.__init__(self)