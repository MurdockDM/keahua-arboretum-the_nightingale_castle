import os
import json
from .get_data import get_saves
from .recreate_class import create_class
from .show_title import print_title
def load_data(arberatum, menu, text="Select a save from above to load", error=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title("Load")
    saves = get_saves()

    
    if len(saves) == 0:
        print("**** There are no Saves to Load ****")
        input("\nPress ENTER to go back to the Main Menu...")
        menu()
    else:
        print("0. Main Menu")

        for i, save in enumerate(saves):
            name = save.split("/")[1].split(".json")[0]
            print(f"{i + 1}. {name}")
        if error:
            print(f"\n* {text} *")
        else:
            print(f"\n{text}")

        choice = input("> ")

        tuple_return = 0
        try:
            choice = int(choice)
            if choice > len(saves) or choice < 0:
                raise ValueError
            else:
                if choice == 0:
                    menu()
                else:
                    selection = saves[choice - 1]
                    name = selection.split('/')[1].split('.json')[0]
                    print(f"Type '{name}' to load this file")
                    text_check = input("> ")
                    if text_check == name:
                        new_class = create_class(selection)
                        menu(f"'{name}' file loaded", new_class)
                    else:
                        raise TypeError

        except ValueError:
            tuple_return = load_data(arberatum, menu, "Please input one of the numbers listed above", error=True)
            return tuple_return
        except TypeError:
            tuple_return = load_data(arberatum, menu, "Incorrect name typed please reselect file to try again", error=True)
            return tuple_return


