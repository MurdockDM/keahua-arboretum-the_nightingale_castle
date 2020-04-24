# Trinity
import animals
import os
# import environments
# from environments import Environment
from animals import Animal
from inspect import isclass
from .select_animal import build_select_animal_menu


def release_animal(arboretum, menu):

    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list, ANIMAL_SELECTION = build_select_animal_menu(
        animal_list)
    animal = animal_instance_list[ANIMAL_SELECTION - 1]
    if ANIMAL_SELECTION > len(animal_instance_list):
        menu()
    else:
        choice = build_select_location_menu(arboretum, animal)

def build_select_location_menu(arboretum, animal, input_text=f"Choose a Biome to release the animal:"):
    os.system('cls' if os.name == 'nt' else 'clear')

    env_char = {
        "rivers": True if hasattr(animal, "likes_freshwater") else False,
        "coastlines": True if hasattr(animal, "likes_salt") else False,
        "forests": True if hasattr(animal, "likes_shade") else False,
        "grasslands": True if hasattr(animal, "likes_sun") else False,
        "mountains": True if hasattr(animal, "likes_high_elevation") else False,
        "swamps": True if hasattr(animal, "likes_stagnant_water") else False
    }
    avalible_location_dict = dict()

    for key, value in env_char.items():
        if value:
            if len(arboretum.__dict__[key]) > 0:
                avalible_location_dict[key] = arboretum.__dict__[key]

    if len(avalible_location_dict.keys()) == 0:
        print("There are no availible locations for {animal.species} to go.")
        print(f"To add a Biome, go back to the main menu and select option 1")
        print("1. Main Menu")
    else:
        i = 1
        avalible_location_list = list()
        for key, value in avalible_location_dict.items():
            for item in value:
                avalible_location_list.append(item)
        
        for i, value in enumerate(avalible_location_list):
            print(f"{i + 1} {value}")

        print(f"{len(avalible_location_list) + 1}. Main Menu")
        print(f"\n\n {input_text} {animal.species}")
        choice = input(">> ")

        try:
            choice = int(choice)
        except ValueError:
            build_select_location_menu(arboretum, animal, "Please provide a number without decimal points to place:")
        else:
            print(choice)
