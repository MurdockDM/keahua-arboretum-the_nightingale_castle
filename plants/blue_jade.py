from .plant import Plant
from interfaces import IStagnant
from interfaces import ISunny
from interfaces import Identifiable

class BlueJade(Plant, IStagnant, ISunny, Identifiable):

    def __init__(self, name):
        Plant.__init__(self, name)
        IStagnant.__init__(self)
        ISunny.__init__(self)
        Identifiable.__init__(self)