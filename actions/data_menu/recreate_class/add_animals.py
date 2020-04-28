import animals
from animals import Animal
from inspect import isclass

def add_animals(env, animal):
    id = animal["id"]

    module = animals.__dict__
    env_list = ""
    for key, value in module.items():
        if isclass(value) and value != Animal:
            env_inst = value(id=f"{id}")
            if animal["species"] == env_inst.species:
                env.add_inhabitant(env_inst)

