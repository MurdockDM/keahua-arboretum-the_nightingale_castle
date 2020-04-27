
import plants
from plants import Plant
import os
from inspect import isclass
from .plant_biomes_menu import plant_biomes


def select_plant_menu(plants_list, main_menu):

    """This function creates the menu of plants to add to a biome"""

    os.system('cls' if os.name == 'nt' else 'clear')
    plant_instance_list = ["" for i in plants_list]

    
    for i, plant in enumerate(plants_list):
        plant_instance_list[i] = plant()
        print(f"{i + 1}. {plant_instance_list[i].species}")

    print(f"{len(plant_instance_list) + 1}. Main Menu")
    choice = input(">> ")
    
    try:
        choice = int(choice)
    except ValueError:
        select_plant_menu(plants_list, "Please use an interger")
    else:
        return (plant_instance_list, choice)

def run_plant_menu(arboretum, main_menu):

    """This function handles plant cultivation for annexed biomes."""

    module = plants.__dict__
    plant_list = []
    for key, value in module.items():
        if isclass(value) and value != Plant:
            plant_list.append(value)

    plant, selection = select_plant_menu(plant_list, main_menu)
    
    if selection > len(plant_list):
        main_menu()
    else:
        plant_biomes(arboretum, plant[selection - 1], main_menu, run_plant_menu)

