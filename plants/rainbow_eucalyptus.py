from .plant import Plant
from interfaces import Identifiable
from interfaces import IShady

class RainbowEucalyptus(Plant, Identifiable, IShady):

    def __init__(self, name = "Rainbow Eucalyptus"):
        Plant.__init__(self, name)
        Identifiable.__init__(self)
        IShady.__init__(self)
        self.image = """
                _,-'"" ""'""`--.
             ,-'          __,,-- \
           ,'    __,--""'""dF      )
          /   .-"Hb_,--""dF      /
        ,'       _Hb ___dF"-._,-'
      ,'      _,-""'""   ""--..__
     (     ,-'                  `.
      `._,'     _   _             ;
       ,'     ,' `-'Hb-.___..._,-'
       \    ,'"Hb.-'HH`-.dHF"
        `--'   "Hb  HH  dF"
                "Hb HH dF
                 "HbHHdF
                  |HHHF
                  |HHH|
                  |HHH|
                  |HHH|
                  |HHH|
                  dHHHb
                .dFd|bHb.               o
      o       .dHFdH|HbTHb.          o /
\  Y  |  \__,dHHFdHH|HHhoHHb.__/     |  Y /
##########################################
            
        """