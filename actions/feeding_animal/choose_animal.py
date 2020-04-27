import sys
import os
from arboretum import Arboretum
from .choose_individual import filter_animals


def build_feeding_animal_menu(arboretum, animal_list, menu):
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animal_instance_list = ["" for i in animal_list]
    print('''  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
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

    choice = input("Choose an option >>")

    try:
        choice = int(choice)
        if choice <= len(animal_instance_list) and choice > 0:
            filter_animals(arboretum, choice, menu)
        elif choice == 0:
            sys.exit()
        elif choice == len(animal_instance_list) + 1:
            menu()
    except ValueError:
        restart_menu = build_feeding_animal_menu(arboretum, animal_list, menu)
        return restart_menu
    else:
        menu()
