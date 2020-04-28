import os
from actions.data_menu.get_data import get_saves
from .show_title import print_title
def delete_data(arberatum, menu, text="Select a save from above to delete", error=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title("Delete")
    saves = get_saves()

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
                print(f"Type '{name}' to delete this file")
                text_check = input("> ")
                if text_check == name:
                    os.remove(selection)
                    menu(f"'{name}'file deleted")
                else:
                    raise TypeError

    except ValueError:
        tuple_return = delete_data(arberatum, menu, "Please input one of the numbers listed above", error=True)
        return tuple_return
    except TypeError:
        tuple_return = delete_data(arberatum, menu, "Incorrect name typed please reselect file to try again", error=True)
        return tuple_return