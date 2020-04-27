import os
from .fed_animal import animal_fed

def choose_prey(individual_choice, list_of_animal_lists, choice, menu, message_text):

    os.system('cls' if os.name == 'nt' else 'clear')


    chosen_animal = list_of_animal_lists[int(
        choice) - 1][int(individual_choice) - 1]
    list_chosen_animal_prey = list(chosen_animal.prey)
    print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |         C h o o s e  a  f o o d  t y p e        |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
    print()
    for i, prey in enumerate(list_chosen_animal_prey):
        print(f'{i +1}. {prey}')


    if message_text != "":
            print(f"\n{message_text}")
            message_text=""
    prey_choice = input(
        f">")

    try:
        prey_choice = int(prey_choice)
        if prey_choice <= len(list_chosen_animal_prey) and prey_choice > 0:
            animal_fed(prey_choice, chosen_animal, list_chosen_animal_prey, menu, message_text)
        else:
            message_text = "*  Please input one of the numbers above  *"
            choose_prey(individual_choice, list_of_animal_lists, choice, menu, message_text)
    except IndexError:
        choose_prey(individual_choice, list_of_animal_lists, choice, menu, message_text)        
