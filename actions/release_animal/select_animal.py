import os

INDEX = 0
def build_select_animal_menu(animal_list, input_text = "Choose an Animal to release"):
    
    """
    Creates Select Animal Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    animal_instance_list = ["" for i in animal_list]
    for i, animal in enumerate(animal_list):
        animal_instance_list[i] = animal()
        print(f"{i + 1}. {animal_instance_list[i].species}")

    print(f"{len(animal_instance_list) + 1}. Main Menu")
    print(input_text)
    choice = input(">> ")
    tuple_return = 0
    try:
        choice = int(choice)
    except ValueError:
        tuple_return = build_select_animal_menu(animal_list, "Please provide a number without decimal points")
        return tuple_return
    return animal_instance_list, choice
 
        