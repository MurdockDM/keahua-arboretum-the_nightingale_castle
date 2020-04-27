# Katie
import os
from environments import Coastline, Forest, Grassland, Mountain, River, Swamp

def annex_habitat(arboretum, menu, message_text):
    os.system('cls' if os.name == 'nt' else 'clear')
    print(" +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print(" |          A n n e x     a     B i o m e          |")
    print(" +-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-++-+")
    print()
    print("0. Main Menu")
    print("1. Coastline")
    print("2. Forest")
    print("3. Grassland")
    print("4. Mountain")
    print("5. River")
    print("6. Swamp")
    print()
    print(message_text)
    choice = input("> ")

    if choice == "1":
        coastline = Coastline()
        arboretum.coastlines.append(coastline)
        menu(f"~+ You just annexed a new Coastline biome +~\n{coastline.image}") 
    elif choice == "2":
        forest = Forest()
        arboretum.forests.append(forest)
        menu(f"~+ You just annexed a new Forest biome +~\n{forest.image}") 
    elif choice == "3":
        grassland = Grassland()
        arboretum.grasslands.append(grassland)
        menu(f"~+ You just annexed a new Grassland biome +~\n{grassland.image}") 
    elif choice == "4":
        mountain = Mountain()
        arboretum.mountains.append(mountain)
        menu(f"~+ You just annexed a new Mountain biome +~\n{mountain.image}") 
    elif choice == "5":
        river = River()
        arboretum.rivers.append(river)
        menu(f"~+ You just annexed a new River biome +~\n{river.image}") 
    elif choice == "6":
        swamp = Swamp()
        arboretum.swamps.append(swamp)
        menu(f"~+ You just annexed a new Swamp biome +~\n{swamp.image}") 
    elif choice == "0":
        menu()   
    else: 
        annex_habitat(arboretum, menu, message_text = "* Please input one of the numbers listed above *")