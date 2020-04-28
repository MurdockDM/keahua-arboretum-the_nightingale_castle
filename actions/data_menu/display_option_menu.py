import os
from .save_data import save_data
from .delete_data import delete_data
from .load_data import load_data
from .show_title import print_title
def display_option_menu(arberatum, menu, text="Choose an option above", error=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title("Data")
    menu_list = ["Main Menu", "Load Data", "Save Data", "Delete Data"]
    for i, item in enumerate(menu_list):
        print(f"{i}. {item}")
    if error:
        print(f"\n* {text} *")
    else:
        print(f"\n{text}")

    choice = input("> ")

    tuple_return = 0
    try:
        choice = int(choice)
        if choice >= len(menu_list) or choice < 0:
            raise ValueError
        else:
            if choice == 0:
                menu()
            elif choice == 1:
                load_data(arberatum, menu)
            elif choice == 2:
                save_data(arberatum, menu)
            elif choice == 3:
                delete_data(arberatum, menu)
    except ValueError:
        tuple_return = display_option_menu(menu, "Please input one of the numbers listed above", error=True)
        return tuple_return