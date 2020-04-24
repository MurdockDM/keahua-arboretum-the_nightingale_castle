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

    animal_instance_list, ANIMAL_SELECTION = build_select_animal_menu(
        animal_list)
    if ANIMAL_SELECTION >= len(animal_instance_list):
        menu()
    else:
        animal = animal_instance_list[ANIMAL_SELECTION - 1]
        choice = build_select_location_menu(arboretum, animal, menu)

