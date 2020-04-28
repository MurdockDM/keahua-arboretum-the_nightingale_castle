import os
from .get_data import get_saves
from .save import save_as, save_new
from .show_title import print_title

def save_data(arberatum, menu, text="Choose an option from above", error=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title("Save")
    already_saved = False
    new_obj = arberatum.__dict__
    
    if new_obj["saved_file"]:
        already_saved = True

    print("0. Main Menu")
    print("1. Save as")
    if already_saved: print("2. Save")


    if error:
        print(f"\n* {text} *")
    else:
        print(f"\n{text}")

    choice = input("> ")
    tuple_return = 0
    try:
        choice = int(choice)
        if choice > 2 or choice < 0:
            raise ValueError
        else:
            if choice == 0:
                menu()
            elif choice == 1:
                save_as(arberatum, menu)
            elif already_saved and choice == 2:
                save_new(arberatum, menu)
            else:
                raise ValueError
    except ValueError:
        tuple_return = save_data(arberatum, menu, "Please input one of the numbers listed above", error=True)
        return tuple_return
    




