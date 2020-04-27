import os
from arboretum import Arboretum
from actions import (annex_habitat, build_facility_report, release_animal)
from actions.report import build_facility_report
from actions.feeding_animal.feed_animal import  feeding_menu

keahua = Arboretum("Keahua Arboretum", "123 Paukauila Lane")

def build_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print(" |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |")
    print(" +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print("\n1. Annex Biome")
    print("2. Release New Animal")
    print("3. Feed Animal")
    print("4. Cultivate New Plant")
    print("5. Show Arboretum Report")
    print("6. Exit")
    print("\nChoose a KILLER option.")


def main_menu():

    """Show Keahua Action Options

    Arguments: None
    """
    build_menu()

    choice = input(">> ")

    if choice == "1":
        annex_habitat(keahua, main_menu)

    elif choice == "2":
        release_animal(keahua, main_menu)

    elif choice == "3":
        feeding_menu(keahua, main_menu)
    # feed

    elif choice == "4":
        main_menu()
    # cultivate

    elif choice == "5":
        build_facility_report(keahua, main_menu)
        pass

    elif choice != "6":
        main_menu()

main_menu()
