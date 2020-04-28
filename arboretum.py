import json
import copy

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
        self.saved_file = None

    def animals(self):
        listOfAllAnimals = []
        allBiomes = [self.rivers, self.coastlines, self.forests,
                     self.mountains, self.swamps, self.grasslands]

        for biome in allBiomes:
            for environment in biome:
                for animal in environment.inhabitants["Animals"]:
                    listOfAllAnimals.append(animal)

        return listOfAllAnimals

    def update_json(self, name = ""):
        new_Obj = copy.deepcopy(self)

        data = json.dumps(new_Obj, default=convert_to_dict)
        file_name = '_'.join(new_Obj.name.lower().split(' ')) if name == "" else name

        with open(f"api/{file_name}.json", "w") as outfile:
            json.dump(data, outfile)




def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """
    category_list = ["forests", "coastlines",
                     "grasslands", "rivers", "mountains", "swamps"]

    if hasattr(obj, "__dict__"):
        new_obj = obj.__dict__
        if hasattr(obj, category_list[0]):
            for category in category_list:
                if len(new_obj[category]) > 0:
                    env_list = new_obj[category]
                    new_obj[category] = []
                    for env in env_list:
                        if hasattr(env, "inhabitants"):
                            inhabitants = env.inhabitants
                            animals = []
                            plants = []
                            key = f"{env.id}"
                            for animal in inhabitants["Animals"]:
                                animals.append({"id": f"{animal.id}","species": animal.species})
                            
                            for plant in inhabitants["Plants"]:
                                plants.append({"id": f"{plant.id}","species": plant.species})
                            new_obj[category].append({
                                "Animals": animals, "Plants": plants, "id": key})

    else:
        new_obj = {}

    return new_obj
