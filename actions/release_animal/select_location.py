import os

def build_select_location_menu(arboretum, animal, menu, input_text=f"Choose a Biome to release the animal:"):
    """
    Builds Location Menu
    """
    os.system('cls' if os.name == 'nt' else 'clear')

    env_char = {
        "rivers": True if hasattr(animal, "likes_freshwater") else False,
        "coastlines": True if hasattr(animal, "likes_salt") else False,
        "forests": True if hasattr(animal, "likes_shade") else False,
        "grasslands": True if hasattr(animal, "likes_sun") else False,
        "mountains": True if hasattr(animal, "likes_high_elevation") else False,
        "swamps": True if hasattr(animal, "likes_stagnant_water") else False
    }

    avalible_location_dict = dict()

    for key, value in env_char.items():
        if value:
            if len(arboretum.__dict__[key]) > 0:
                avalible_location_dict[key] = arboretum.__dict__[key]

    if len(avalible_location_dict.keys()) == 0:
        print(f"There are no availible locations for {animal.species} to go.")
        print(f"To add a Biome, from the main menu select option 1")
        print("Press Enter to go back to the main menu")
        input(">>")
        menu()
    else:
        i = 1
        avalible_location_list = list()
        for key, value in avalible_location_dict.items():
            for item in value:
                avalible_location_list.append(item)
        
        for i, value in enumerate(avalible_location_list):
            print(f"{i + 1}. {str(value).capitalize()} ({len(value.inhabitants['Animals'])} animals)")

        print(f"{len(avalible_location_list) + 1}. Main Menu")
        # print(f"\n\n {input_text} {animal.species}")

        print("Press enter to cotinue...")
        choice = input(">> ")
        menu()
        # try:
        #     choice = int(choice)
        # except ValueError:
        #     build_select_location_menu(arboretum, animal, animal.species, "Please provide a number without decimal points to place:")
        # else:
        #     print(choice)
