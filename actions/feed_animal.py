# import os
# from animals import Gecko, Goose, Kikakapu, Opeapea, Pueo, RiverDolphin, Spider, Ulae

# def feeding_menu(arboretum, menu):
#     os.system('cls' if os.name == 'nt' else 'clear')
#     print("1. Gold Dust Day Gecko")
#     print("2. Nene Goose")
#     print("3. Kīkākapu ")
#     print("4. Ope'ape'a")
#     print("5. Pueo")
#     print("6. River Dolphin")
#     print("7. Hawaiian Happy-Face Spider")
#     print("8. 'Ulae")



#     choice = input("Choose the animal you want to feed > ")

#     if choice == "1":
       
#     if choice == "2":
        
#     if choice == "3":
        
#     if choice == "4":
        
#     if choice == "5":
        
#     if choice == "6":
        
#     if choice == "7":

#     if choice == "8":

#     menu()

import animals
import os
from animals import Animal
from inspect import isclass
from arboretum import Arboretum

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



    choice = input("Choose an option >>")

def feeding_menu(arboretum):
    
    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list = build_select_animal_menu(animal_list)