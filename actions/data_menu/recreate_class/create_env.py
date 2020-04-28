import environments
from environments import Environment
from inspect import isclass
from .add_animals import add_animals
from .add_plants import add_plants
def create_env(env_info, env_key_name):
    info = env_info
    id = env_info["id"]

    module = environments.__dict__
    env_list = ""
    for key, value in module.items():
        if isclass(value) and value != Environment:
            env_inst = value(id=f"{id}")
            if env_inst.name == env_key_name[:-1]:
                env_list = env_inst

    for animal in env_info["Animals"]:
        add_animals(env_list, animal)


    for plant in env_info["Plants"]:
        add_plants(env_list, plant)
    
    return env_list
