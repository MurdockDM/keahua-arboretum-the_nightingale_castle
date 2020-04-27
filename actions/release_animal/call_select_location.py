from .select_location import build_select_location_menu

def call_select_location(animal_instance_list, animal_selection, arboretum, menu, other_text=False):
    """
    A method to call the select location menu so that it can be used recursively
    """
    
    animal = animal_instance_list[animal_selection - 1]
    env = build_select_location_menu(arboretum, animal, menu, other_text=other_text)
    if env != None:
        if env == "menu":
            menu()
        elif env.animal_capacity > len(env.inhabitants["Animals"]):
            env.add_inhabitant(animal)
            
            menu(f"You released {animal.species} ({str(animal.id)[:8]}) to {str(env.name).capitalize()} [{str(env.id)[:8]}]")
        else:
            call_select_location(animal_instance_list, animal_selection, arboretum, menu, "****   That biome is not large enough   ****\n****     Please choose another one      ****\n ")