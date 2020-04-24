# Trinity
import animals
import os
# import environments
# from environments import Environment
from animals import Animal
from inspect import isclass
from .select_animal import build_select_animal_menu
from .select_location import build_select_location_menu


def release_animal(arboretum, menu):

    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list, animal_selection = build_select_animal_menu(animal_list)
    
    if animal_selection > len(animal_instance_list):
        menu()
    else:
       call_select_location(animal_instance_list, animal_selection, arboretum, menu)

        

def call_select_location(animal_instance_list, animal_selection, arboretum, menu, other_text=False):
    animal = animal_instance_list[animal_selection - 1]
    env = build_select_location_menu(arboretum, animal, menu, other_text="****   That biome is not large enough   **** \n ****     Please choose another one      ****")
    if env != None:
        if env == "menu":
            menu()
        elif env.animal_capacity > len(env.inhabitants["Animals"]):
            env.add_inhabitant(animal)
            menu()
        else:
            call_select_location(animal_instance_list, animal_selection, arboretum, menu, "****   That biome is not large enough   ****\n****     Please choose another one      ****")

