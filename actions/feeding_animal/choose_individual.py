import os
from .choose_prey import choose_prey
from arboretum import Arboretum

def filter_animals(arboretum, choice, menu):

    all_animals_all_biomes = Arboretum.animals(arboretum)

    geckos = []
    geese = []
    kikakapus = []
    opeapeas = []
    pueos = []
    river_dolphins = []
    spiders = []
    ulaes = []

    list_of_animal_lists = [geckos, geese, kikakapus,
                            opeapeas, pueos, river_dolphins, spiders, ulaes]

    for animal in all_animals_all_biomes:
        if animal.species == "Gold Dust Day Gecko":
            geckos.append(animal)
        if animal.species == "Nene Goose":
            geese.append(animal)
        if animal.species == "Kīkākapu":
            kikakapus.append(animal)
        if animal.species == "Ope'ape'a":
            opeapeas.append(animal)
        if animal.species == "Pueo":
            pueos.append(animal)
        if animal.species == "River Dolphin":
            river_dolphins.append(animal)
        if animal.species == "Hawaiian Happy-Face Spider":
            spiders.append(animal)
        if animal.species == "'Ulae":
            ulaes.append(animal)

    os.system('cls' if os.name == 'nt' else 'clear')

    selected_list = list_of_animal_lists[int(choice) - 1]

    if len(selected_list) < 1:
        user_break = input(
            "There does not appear to any of this type of animal \n \n Press any key to try again")
        if user_break:
            filter_animals(arboretum, choice, menu)

    else:
        print(''' +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+
 |  K  e  a  h  u  a    A  r  b  o  r  e  t  u  m  |
 +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+ ''')
        for i, animal in enumerate(selected_list):
            print(f"{i+1}. {animal.species} {str(animal.id).split('-')[0] }")
        print(f"{len(selected_list) + 1}. Main Menu")

        individual_choice = input("which animal do you want to feed? >>")

        try:
            individual_choice = int(individual_choice)
            if individual_choice > 0 and individual_choice <= len(selected_list):
                choose_prey(individual_choice,list_of_animal_lists, choice, menu)
            elif individual_choice == len(selected_list) + 1:
                menu()
            else:
                filter_animals(arboretum, choice, menu)            
        except IndexError:
            filter_animals(arboretum, choice, menu)
