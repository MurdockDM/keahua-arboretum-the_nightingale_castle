import os
from arboretum import Arboretum
from actions import (annex_habitat, build_facility_report,
                     release_animal, run_plant_menu, show_data)
from actions.report import build_facility_report
from actions.feeding_animal.feed_animal import feeding_menu




def build_menu(message_text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')

    if message_text != "":
        print(f'\n {message_text}')

    print("\n1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Data Menu")
    print("7. Exit")
    print("\nChoose a KILLER option.")

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def main_menu(message_text="", keahua_class=""):
    if keahua_class != "":
        global keahua
        keahua = keahua_class

    """Show Keahua Action Options

    Arguments: None
    """
    build_menu(message_text)

    choice = input("> ")

    if choice == "1":
        annex_habitat(keahua, main_menu,
                      message_text="Choose a biome to annex")

    elif choice == "2":
        release_animal(keahua, main_menu)

    elif choice == "3":
        feeding_menu(keahua, main_menu)
    # feed

    elif choice == "4":
        run_plant_menu(keahua, main_menu)

    elif choice == "5":
        build_facility_report(keahua, main_menu)
        pass

    elif choice == "6":
        show_data(keahua, main_menu)

    elif choice != "7":
        main_menu()

main_menu()
