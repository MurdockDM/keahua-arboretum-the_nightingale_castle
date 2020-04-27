import os

def animal_fed(prey_choice, chosen_animal, list_chosen_animal_prey, menu, message_text):

    os.system('cls' if os.name == 'nt' else 'clear')

    print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |      F e e d i n g  C o n f i r m a t i o n     |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
    if message_text != "":
            print(f"\n{message_text}")
            message_text=""
    print()
    user_any_entry = input(
        f"The {chosen_animal.species} ate {list_chosen_animal_prey[int(prey_choice) - 1]} \n \nPress ENTER to go back to the main menu...")

    menu(message_text = " ~+  You just fed an animal  +~ ")
