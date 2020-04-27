# Andrew
import os

def build_facility_report(arboretum, menu):

    os.system('cls' if os.name == 'nt' else 'clear')

    for coastline in arboretum.coastlines:
        print(f'\nCoastline [{str(coastline.id)[:8]}]')
        for animal in coastline.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in coastline.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    for forest in arboretum.forests:
        print(f'\nForest [{str(forest.id)[:8]}]')
        for animal in forest.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in forest.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    for grassland in arboretum.grasslands:
        print(f'\nGrassland [{str(grassland.id)[:8]}]')
        for animal in grassland.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in grassland.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    for mountain in arboretum.mountains:
        print(f'\nMountain [{str(mountain.id)[:8]}]')
        for animal in mountain.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in mountain.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    for river in arboretum.rivers:
        print(f'\nRiver [{str(river.id)[:8]}]')
        for animal in river.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in river.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')
        
    for swamp in arboretum.swamps:
        print(f'\nSwamp [{str(swamp.id)[:8]}]')
        for animal in swamp.inhabitants["Animals"]:
            print(f'    {str(animal).split(" ")[0]} ({str(animal).split(" ")[1][:8]})')
        for plant in swamp.inhabitants["Plants"]:
            print(f'    {plant.species} ({str(plant.id).split("-")[0]})')

    choice = input("\nPress ENTER to go back to main menu...")

    if choice == "":
        menu("You just viewed the report")