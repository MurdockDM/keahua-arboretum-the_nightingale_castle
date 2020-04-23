from .plant import Plant
from interfaces import Identifiable
from interfaces import IHighElevation

class BlueJade(Plant, Identifiable, IHighElevation):

    def __init__(self, name):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        IHighElevation.__init__(self)