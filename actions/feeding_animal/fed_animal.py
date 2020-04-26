import os

def animal_fed(prey_choice, chosen_animal, list_chosen_animal_prey, menu):

    os.system('cls' if os.name == 'nt' else 'clear')

    print('''  +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')

    user_any_entry = input(
        f"The {chosen_animal} ate {list_chosen_animal_prey[int(prey_choice) - 1]} \n \n Press any key to return to the main menu...")

    menu()
