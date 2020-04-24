# Katie
import os
from environments import Coastline, Forest, Grassland, Mountain, River, Swamp

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. Coastline")
    print("2. Forest")
    print("3. Grassland")
    print("4. Mountain")
    print("5. River")
    print("6. Swamp")

    choice = input("Choose your habitat > ")

    if choice == "1":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
        print(len(arboretum.coastlines))
    if choice == "2":
        forest = Forest()
        arboretum.forests.append(forest)
        print(len(arboretum.coastlines))
        print(len(arboretum.forests))
    if choice == "3":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
    if choice == "4":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
    if choice == "5":
        river = River()
        arboretum.rivers.append(river)
    if choice == "6":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
