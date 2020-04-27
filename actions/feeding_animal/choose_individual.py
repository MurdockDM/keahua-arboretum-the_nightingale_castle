import os
from .choose_prey import choose_prey
from arboretum import Arboretum 


def filter_animals(arboretum, choice, menu, animal_list, selected_list, list_of_animal_lists, message_text):

    
    os.system('cls' if os.name == 'nt' else 'clear')


    print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |            U n i q u e  A n i m a l s           |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
        
        
    print()
    for i, animal in enumerate(selected_list):
            print(f"{i+1}. {animal.species} {str(animal.id).split('-')[0] }")
    print("0. Main Menu")

    if message_text != "":
            print(f"\n{message_text}")
            message_text=""
    individual_choice = input(">")

    try:
        individual_choice = int(individual_choice)
        if individual_choice > 0 and individual_choice <= len(selected_list):
            choose_prey(individual_choice,list_of_animal_lists, choice, menu, message_text = "Choose something to feed to the animal")
        elif individual_choice == 0:
            menu()
        else:
            message_text = "*  Please input one of the numbers above  *"
            filter_animals(arboretum, choice, menu, animal_list, selected_list, list_of_animal_lists, message_text)            
    except IndexError:
        filter_animals(arboretum, choice, menu, animal_list, selected_list, list_of_animal_lists, message_text)
