import plants
from plants import Plant
from inspect import isclass

def add_plants(env, plant):
    id = plant["id"]

    module = plants.__dict__
    env_list = ""
    for key, value in module.items():
        if isclass(value) and value != Plant:
            env_inst = value(id=f"{id}")
            if plant["species"] == env_inst.species:
                env.add_inhabitant(env_inst)

