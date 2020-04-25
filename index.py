import os
from arboretum import Arboretum
from actions import (annex_habitat, build_facility_report, release_animal, run_plant_menu)
from actions.report import build_facility_report

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Annex Habitat")
    print("2. Release Animal into Habitat")
    print("3. Feed Animal")
    print("4. Add Plant to Habitat")
    print("5. Display Facility Report")
    print("6. Exit")


def main_menu():
    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()
    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua, main_menu)

    if choice == "2":
        release_animal(keahua, main_menu)

    if choice == "3":
        pass
    # feed

    if choice == "4":
        run_plant_menu(keahua, main_menu)

    if choice == "5":
        build_facility_report(keahua)
        pass

    # what if == 6 ? ... close the program
    # does this work??

    # if choice != "6":
    #     main_menu()

main_menu()
