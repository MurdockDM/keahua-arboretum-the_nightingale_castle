class Environment:
    def __init__(self, name, animal_capacity, plant_capacity):
        self.inhabitants = {"Animals": [], "Plants": []}
        self.name = name
        self.animal_capacity = animal_capacity
        self.plant_capacity = plant_capacity