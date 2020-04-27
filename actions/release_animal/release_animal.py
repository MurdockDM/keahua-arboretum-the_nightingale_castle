# Trinity
import animals
import os
# import environments
# from environments import Environment
from animals import Animal
from inspect import isclass
from .select_animal import build_select_animal_menu
from .call_select_location import call_select_location

def release_animal(arboretum, menu):

    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list, animal_selection = build_select_animal_menu(animal_list)
    
    if animal_selection == 0:
        menu()
    else:
       call_select_location(animal_instance_list, animal_selection, arboretum, menu)

        


