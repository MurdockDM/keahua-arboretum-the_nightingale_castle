from .plant import Plant
from interfaces import Identifiable
from interfaces import ISunny

class Silversword(Plant, Identifiable, ISunny):

    def __init__(self, name):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        ISunny.__init__(self)