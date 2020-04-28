import json
from .create_env import create_env
from arboretum import Arboretum


def create_class(file_name):
    category_dict = {"forests": [], "coastlines": [],
                     "grasslands": [], "rivers": [], "mountains": [], "swamps": []}

    with open(file_name) as JSON:
        data = json.loads(json.load(JSON))

    arb_inst = Arboretum(data["name"], data["address"])

    for key, env_name in data.items():
        envs_list = []
        if key in category_dict.keys():
            for env in env_name:
                envs_list.append(create_env(env, key))
            setattr(arb_inst, key, envs_list)
    
    setattr(arb_inst, "saved_file", file_name.split('/')[1].split('.json')[0])
    return arb_inst

