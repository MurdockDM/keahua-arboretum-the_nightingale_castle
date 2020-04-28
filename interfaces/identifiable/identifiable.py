from uuid import uuid1

class Identifiable:
    def __init__(self, id):
      if id == "":
        self.id = uuid1()
      else:
        self.id = id
