import os
from environments import River
# maybe import arboretum??

def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")
    # print forest and mountain?

    choice = input("Choose your habitat > ")

    if choice == "1":
        river = River()
        arboretum.rivers.append(river)
    if choice == "2":
        pass
