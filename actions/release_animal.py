# Trinity
import animals
import os
from animals import Animal
from inspect import isclass

ANIMAL_SELECTION = 0

def build_select_animal_menu(animal_list):
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animal_instance_list = ["" for i in animal_list]

    for i, animal in enumerate(animal_list):
        animal_instance_list[i] = animal()
        print(f"{i + 1}. {animal_instance_list[i].species}")

    print(f"{len(animal_instance_list) + 1}. Main Menu")
    print("0. Exit Application")

def release_animal(arboretum):

    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list = build_select_animal_menu(animal_list)