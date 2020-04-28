import os
from actions.data_menu.get_data import get_saves
from actions.data_menu.show_title import print_title
def save_as(arberatum, menu, text="", error=False):
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title("Save")
    if error:
        print(f"\n* {text} *")
    print("0. Main Menu")
    print(f"\nEnter name for Save")

    file_name = input("> ")

    tuple_return = 0
    try:
        if file_name == "0":
            menu()
        elif not file_name:
            raise ValueError("Please Enter a name")
        else:
            name = '_'.join(file_name.lower().split(' '))
            if f"api/{name}.json" in get_saves():
                raise ValueError(f"{file_name} is Already Taken")
            else:
                arberatum.update_json(name)
                arberatum.saved_file = name
                menu("~+ Saved Data +~")
    except ValueError as taco:
        tuple_return = save_as(arberatum, menu, taco, error=True)
        return tuple_return