import os
from .print_title import print_title

def build_select_location_menu(arboretum, animal, menu, input_text=f"Choose a Biome to release", other_text=False, error=False):
    """
    Builds Location Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print_title()
    env_char = {
        "rivers": True if hasattr(animal, "likes_freshwater") else False,
        "coastlines": True if hasattr(animal, "likes_salt") else False,
        "forests": True if hasattr(animal, "likes_shade") else False,
        "grasslands": True if hasattr(animal, "likes_sun") else False,
        "mountains": True if hasattr(animal, "likes_high_elevation") else False,
        "swamps": True if hasattr(animal, "likes_stagnant_water") else False
    }

    avalible_location_dict = dict()
    locations = []
    for key, value in env_char.items():
        if value:
            locations.append(key.capitalize())
            if len(arboretum.__dict__[key]) > 0:
                avalible_location_dict[key] = arboretum.__dict__[key]
    print(avalible_location_dict)

    if len(avalible_location_dict.keys()) == 0:
        string_length = len(animal.species) // 2
        empty_string = " " * string_length
        os.system('cls' if os.name == 'nt' else 'clear')
        print_title(f"****    There are no availible locations for to {animal.species} go    ****\n**** {empty_string}To add a Biome, from the main menu select option 1{empty_string} ****\n****        The following are places {animal.species} can live         ****")
        print("\n".join(locations))
        input("\nPress ENTER to go back to main menu…")
        menu()
    else:
        i = 1
        avalible_location_list = list()
        for key, value in avalible_location_dict.items():
            for item in value:
                avalible_location_list.append(item)
        if other_text:
            print(other_text)

        print(f"0. Main Menu")
        for i, value in enumerate(avalible_location_list):
            print(f"{i + 1}. {str(value).capitalize()} [{str(value.id)[:8]}] ({len(value.inhabitants['Animals'])} animals)")
        dire_str = f"{input_text} {animal.species} ({str(animal.id)[:8]})"
        if error:
            print(f"\n* {dire_str} *")
        else:
            print(f"\n{dire_str}")


        choice = input("> ")
        tuple_return = 0
        try:
            choice = int(choice)
            if choice > len(avalible_location_list):
                raise ValueError
        except ValueError:
            tuple_return = build_select_location_menu(arboretum, animal, animal.species, "Please input one of the numbers listed above to place", error=True)

            return tuple_return

        return  "menu" if choice == 0 else avalible_location_list[choice - 1]
