import sys
import os
from arboretum import Arboretum
from .choose_individual import filter_animals


def build_feeding_animal_menu(arboretum, animal_list, menu, message_text):
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    
    animal_instance_list = ["" for i in animal_list]
    print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |           Choose an animal to feed              |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')

    print()
    for i, animal in enumerate(animal_list):
        animal_instance_list[i] = animal()
        print(f"{i + 1}. {animal_instance_list[i].species}")


    print("0. Main Menu")


    
    if message_text != "":
            print(f"\n{message_text}")
            message_text=""
    choice = input(">")

    all_animals_all_biomes = Arboretum.animals(arboretum)

    geckos = []
    geese = []
    kikakapus = []
    opeapeas = []
    pueos = []
    river_dolphins = []
    spiders = []
    ulaes = []

    list_of_animal_lists = [geckos, geese, kikakapus,
                            opeapeas, pueos, river_dolphins, spiders, ulaes]

    for animal in all_animals_all_biomes:
        if animal.species == "Gold Dust Day Gecko":
            geckos.append(animal)
        if animal.species == "Nene Goose":
            geese.append(animal)
        if animal.species == "Kīkākapu":
            kikakapus.append(animal)
        if animal.species == "Ope'ape'a":
            opeapeas.append(animal)
        if animal.species == "Pueo":
            pueos.append(animal)
        if animal.species == "River Dolphin":
            river_dolphins.append(animal)
        if animal.species == "Hawaiian Happy-Face Spider":
            spiders.append(animal)
        if animal.species == "'Ulae":
            ulaes.append(animal)
    
   

    try:
        choice = int(choice)
        
        selected_list = list_of_animal_lists[int(choice) - 1]
        
        if choice == 0:
            menu()
        elif len(selected_list) == 0:
            message_text = "****  There does not appear to be any of this type of animal  ****\n \n          ****  Please choose another  ****\n"
            build_feeding_animal_menu(arboretum, animal_list, menu, message_text)
        elif choice <= len(animal_instance_list) and choice > 0:
            filter_animals(arboretum, choice, menu, animal_list, selected_list, list_of_animal_lists, message_text = "\nwhich animal do you want to feed?") 
    except ValueError:
        message_text = "*  Please input one of the numbers above  *"
        restart_menu = build_feeding_animal_menu(arboretum, animal_list, menu, message_text)
        return restart_menu 
    except IndexError:
        message_text = "*  Please input one of the numbers above  *"
        build_feeding_animal_menu(arboretum, animal_list, menu, message_text)       
    else:
        message_text = "*  Please input one of the numbers above  *"
