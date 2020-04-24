![Keahua Landscape](./keahua.jpeg)

# Keahua Arboretum

You and your friends have decided to connect with the earth again and abandon your reliance on technology and urban vices. You have decided to move to Hawaii and join the land management team for the Keahua Arboretum.

You and the other foresters and land managers will be using this application to track the growth and maintainance of the arboretum.

# Getting Started

1. Clone the repository
1. `cd` into the project directory
1. Run the command `pip install -r requirements.txt`
1. Run the command `python index.py` to start the application

# Keahua Inventory and Land Lifeline Electronic Repository (KILLER)

Fancy web applications are so 2018. Command line applications provide a much more hands-on, personal, bespoke, artisinal experience when managing an arboretum like Keahua. Therefore, even though you are casting off your digital personas to lead a life connected with the land, you still want to use your hard-earned skills as developers to make management of the land as efficient as possible.

Here are the main features of the application.

## Main Menu

When KILLER is first executed, the welcome page is a main menu of options.

The user can select one of the following by inputting the corresponding number:

1. Annex Biome
2. Release New Animal
3. Feed Animal
4. Cultivate New Plant
5. Show Arboretum Report
6. Exit
<br/><br/>
### Biome Annex Sub-Menu
---

If the user chooses option 1, then the following menu is displayed

```sh
1. Mountain
2. Swamp
3. Grassland
4. Forest
5. River

Choose what you want to annex.
> _
```

When the user makes a choice, a new biome will be created in the arboretum.
<br/><br/>
### Animal Menu
---
If the user chooses 2 from the main menu, then they will see the following menu, with the animals listed.

```html
1. Gold Dust Day Gecko
2. River Dolphin
3. Nene Goose
4. Kīkākapu
5. Pueo
6. 'Ulae
7. Ope'ape'a
8. Happy-Face Spider

Choose animal.
> _
```

When the user enters in the number of the animal they would like to add, then all of the locations in which the animal can be stored are displayed along with the current number of animals in each location.

```sh
1. Mountain (2 animals)
2. Forest (4 animals)
2. Forest (0 animals)

Where would you like to place the animal?
> _
```

If the user chose to place them in a location that would be over capacity if they were placed there, an error message will appear, and they will see the menu again.

```html
****   That biome is not large enough   ****
****     Please choose another one      ****

1. Mountain (2 animals)
2. Forest (4 animals)
3. Forest (0 animals)

Where would you like to release the Ope'ape'a?
> _
```
<br/><br/>
### Animal Feeding Menu
---
If the user chooses 3 from the main menu, then they will see the following menu, with the animals listed.

```html
1. Gold Dust Day Gecko
2. River Dolphin
3. Nene Goose
4. Kīkākapu
5. Pueo
6. 'Ulae
7. Ope'ape'a
8. Happy-Face Spider

Choose animal to feed.
> _
```

When the user chooses an animal, another menu appears showing the specific food that the animal can be fed.

```html
1. Trout
2. Mackarel
3. Salmon
4. Sardine

What is on the menu for the River Dolphin today?
> _
```

Once the user chooses a food item, they are presented with a message.

```html
The river dolphin ate salmon for a meal.

Press any key to return to the main menu...
```
<br/><br/>
### Plant Cultivation Menu
---
If the user chooses 4 from the main menu, then they will see the following menu, with the plants listed.

```html
1. Mountain Apple Tree
2. Silversword
3. Rainbow Eucalyptus Tree
4. Blue Jade Vine

Choose plant to cultivate.
> _
```

When the user makes a choice, all of the locations in which the plants can be planted will be displayed along with the current number of plants in each location.

```sh
1. Grassland (5 plants)
2. Swamp (2 plants)
3. Swamp (9 plants)
4. Swamp (0 plants)

Where would you like to plant the Sun Jade Vine?
> _
```

If the user chooses to place the plant in a location that would be over capacity if it were placed there, an error message will be displayed, and they will see the menu again.

```html
****   That biome is not large enough   ****
****     Please choose another one      ****

1. Grassland (5 plants)
2. Swamp (2 plants)
3. Swamp (9 plants)
4. Swamp (0 plants)

Where would you like to plant the Sun Jade Vine?
> _
```
<br/><br/>
### Arboretum Report Menu
---
Choosing this option will list all existing biomes and then list all animals and plants in that biome. The unique ID of each biome, animal, and plant will be displayed in paretheses. 

```html
River [157b2efe]
    River Dolphin (133619c4)

Mountain [bdf33960]
    Ope'ape'a (bf9ad976)
    Ope'ape'a (f9dd0afa)
    Mountain Apple Tree (h91d77a0)


Press any key to continue...
```
<br/><br/>
# Team Sketchboard

![Team Sketchboard](./SketchBoard.png)