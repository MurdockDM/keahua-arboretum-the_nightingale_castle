from .plant import Plant
from interfaces import Identifiable
from interfaces import IShady

class RainbowEucalyptus(Plant, Identifiable, IShady):

    def __init__(self, name):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        IShady.__init__(self)