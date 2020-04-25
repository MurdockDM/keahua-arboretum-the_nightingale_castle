import animals
import os
from animals import Animal
from inspect import isclass
from arboretum import Arboretum

ANIMAL_SELECTION = 0

def build_feeding_animal_menu(arboretum, animal_list):
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animal_instance_list = ["" for i in animal_list]
    print(''' 
___________               .___.__                 ___________.___                
\_   _____/___   ____   __| _/|__| ____    ____   \__    ___/|   | _____   ____  
 |    __)/ __ \_/ __ \ / __ | |  |/    \  / ___\    |    |   |   |/     \_/ __ \ 
 |     \\  ___/\  ___// /_/ | |  |   |  \/ /_/  >   |    |   |   |  Y Y  \  ___/ 
 \___  / \___  >\___  >____ | |__|___|  /\___  /    |____|   |___|__|_|  /\___  >
     \/      \/     \/     \/         \//_____/                        \/     \/  ''')

    for i, animal in enumerate(animal_list):
        animal_instance_list[i] = animal()
        print(f"{i + 1}. {animal_instance_list[i].species}")

    print(f"{len(animal_instance_list) + 1}. Main Menu")
    print("0. Exit Application")
    
    someanimals = Arboretum.animals(arboretum)
    print(someanimals)

    choice = input("Choose an option >>")


def feeding_menu(arboretum):
    
    module = animals.__dict__
    animal_list = []
    for key, value in module.items():
        if isclass(value) and value != Animal:
            animal_list.append(value)

    animal = None

    animal_instance_list = build_feeding_animal_menu(arboretum, animal_list)


# def filter_animals(arboretum, choice):

#     all_animals_all_biomes = Arboretum.animals(arboretum) 

#     geckos = []
#     geese = []
#     kikakapus = []
#     opeapeas = []
#     pueos = []
#     river_dolphins = []
#     spiders = []
#     ulaes = []   

#     for animal in all_animals_all_biomes:

