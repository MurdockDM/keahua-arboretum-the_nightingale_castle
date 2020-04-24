# Andrew
def build_facility_report(arboretum, menu):
    for coastline in arboretum.coastlines:
        print(f'\nCoastline [{str(coastline.id)[:8]}]')

    for forest in arboretum.forests:
        print(f'\nForest [{str(forest.id)[:8]}]')

    for grassland in arboretum.grasslands:
        print(f'\nGrassland [{str(grassland.id)[:8]}]')

    for mountain in arboretum.mountains:
        print(f'\nMountain [{str(mountain.id)[:8]}]')

    for river in arboretum.rivers:
        print(f'\nRiver [{str(river.id)[:8]}]')
        
    for swamp in arboretum.swamps:
        print(f'\nSwamp [{str(swamp.id)[:8]}]')

    # input("\n\nPress any key to continue...")

    choice = input("\nPress Enter to go back to main menu")

    if choice == "":
        menu()