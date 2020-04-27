import os
from .print_title import print_title
INDEX = 0
def build_select_animal_menu(animal_list, input_text = "Choose an Animal to release"):
    
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title()

    animal_instance_list = ["" for i in animal_list]
    print(f"0. Main Menu")
    for i, animal in enumerate(animal_list):
        animal_instance_list[i] = animal()
        print(f"{i + 1}. {animal_instance_list[i].species}")

    print(f"\n{input_text}")
    choice = input("> ")
    tuple_return = 0
    try:
        choice = int(choice)
        if choice > len(animal_instance_list) + 1:
            raise ValueError
    except ValueError:
        tuple_return = build_select_animal_menu(animal_list, "* Please input one of the numbers listed above *")
        return tuple_return
    return animal_instance_list, choice
 
        