class Arboretum:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.rivers = []
        self.grasslands = []
        self.forests = []
        self.mountains = []
        self.coastlines = []
        self.swamps = []

    def animals(self):
        listOfAllAnimals = []
        allBiomes = [self.rivers, self.coastlines, self.forests, self.mountains, self.swamps, self.grasslands]
        
        for biome in allBiomes:
            for environment in biome:
                for animal in environment.inhabitants["Animals"]:
                    listOfAllAnimals.append(animal)

        return listOfAllAnimals        