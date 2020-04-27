import os
from .fed_animal import animal_fed

def choose_prey(individual_choice, list_of_animal_lists, choice, menu):

    os.system('cls' if os.name == 'nt' else 'clear')

    chosen_animal = list_of_animal_lists[int(
        choice) - 1][int(individual_choice) - 1]
    list_chosen_animal_prey = list(chosen_animal.prey)
    print('''  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
    for i, prey in enumerate(list_chosen_animal_prey):
        print(f'{i +1} {prey}')

    prey_choice = input(
        f"\n Choose something to feed to the {chosen_animal.species} ")

    try:
        prey_choice = int(prey_choice)
        if prey_choice <= len(list_chosen_animal_prey) and prey_choice > 0:
            animal_fed(prey_choice, chosen_animal, list_chosen_animal_prey, menu)
        else:
            choose_prey(individual_choice, list_of_animal_lists, choice, menu)
    except IndexError:
        choose_prey(individual_choice, list_of_animal_lists, choice, menu)        
