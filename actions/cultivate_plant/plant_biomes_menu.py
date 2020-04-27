import os
# from plant_menu import run_plant_menu

def plant_biomes(arboretum, plant, menu, plant_menu, input_text=f"Choose a Biome to plant le plant:"):
    """Displays the appropriate biomes for the plant"""
    os.system('cls' if os.name == 'nt' else 'clear')

    env_char = {
        "rivers": True if hasattr(plant, "likes_freshwater") else False,
        "coastlines": True if hasattr(plant, "likes_salt") else False,
        "forests": True if hasattr(plant, "likes_shade") else False,
        "grasslands": True if hasattr(plant, "likes_sun") else False,
        "mountains": True if hasattr(plant, "likes_high_elevation") else False,
        "swamps": True if hasattr(plant, "likes_stagnant_water") else False
    }

    biomes_dict = dict()
    compatible_environment_types = list()
    for k, v in env_char.items():
        if v == True:
            compatible_environment_types.append(k)

    for k, v in arboretum.__dict__.items():
        if k in compatible_environment_types and len(v) > 0:
            for i, value in enumerate(v):
                biomes_dict[f"{value.name} [{str(value.id)[:8]}]"] = value

    biomes_dict_list = list(enumerate(biomes_dict.items()))

    if len(biomes_dict) == 0:
        print("There are no available environments for this plant")
        print("Press ENTER to return to the main menu and annex more environments")
        input(">")
        menu()
    else:
        print(input_text)
        for i, v in biomes_dict_list:
            print(f"{i+1}. {v[0].capitalize()} ({len((v[1].inhabitants)['Plants'])} plants)")
        print(f"{len(biomes_dict.items())+1}. Back to Plants")
        print(f"{len(biomes_dict.items())+2}. Main Menu")
        choice = input(">> ")

        if choice == int(choice):
            plant_biomes(arboretum, plant, menu, "Please make your selection with an interger.")
        elif int(choice) == len(biomes_dict.items())+1:
            plant_menu(arboretum, menu)
        elif int(choice) >= len(biomes_dict.items())+2:
            menu()
        else:
            biome_class = biomes_dict_list[int(choice)-1][1][1]
            if len(biome_class.inhabitants["Plants"]) < biome_class.plant_capacity:
                biome_class.inhabitants["Plants"].append(plant)
                menu(f"Successfully added {plant.species}")
            else:
                plant_biomes(arboretum, plant, menu, "That biome is at carrying capacity, please try again!")
                