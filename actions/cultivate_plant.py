
import plants
from plants import Plant
import os
from inspect import isclass


def build_select_plant_menu(plants_list):
    """This function creates the menu of plants to add to a biome"""
    os.system('cls' if os.name == 'nt' else 'clear')
    plant_instance_list = ["" for i in plants_list]

    
    for i, plant in enumerate(plants_list):
        plant_instance_list[i] = plant()
        print(f"{i + 1}. {plant_instance_list[i].species}")

    print(f"{len(plant_instance_list) + 1}. Main Menu")
    print("0. Exit Application")

def cultivate_plant(arboretum):

    module = plants.__dict__
    plant_list = []
    for key, value in module.items():
        if isclass(value) and value != Plant:
            plant_list.append(value)

    build_select_plant_menu(plant_list)
    print(plant_list)
    choice = input(">> ")
    if choice == "5":
        print("Something happened")

