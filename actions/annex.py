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
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
