import animals
import os
import sys
from animals import Animal
from inspect import isclass
from arboretum import Arboretum
from .choose_animal import build_feeding_animal_menu


def feeding_menu(arboretum, menu):

    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list = build_feeding_animal_menu(
        arboretum, animal_list, menu)
