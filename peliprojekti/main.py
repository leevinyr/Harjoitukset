import random
import os
import json
from classes import Entity, Player, Item, Room
from items import all_items

player = Player("", 0, "")

# Generoi satunnaisen määrän item-olioita mahdollisia tavaroita sisältävästä listasta
def generate_items():
    room_items = []

    for i in range(0, random.randint(1, 4)):
        random_item = random.randint(0, len(all_items)-1)
        room_items.append(all_items[random_item])
        all_items.pop(random_item)

    return room_items

Entryway = Room("Entryway", generate_items())
Kitchen = Room("Kitchen", generate_items())
Living_room = Room("Living room", generate_items())
Bathroom = Room("Bathroom", generate_items())
Attic = Room("Attic", generate_items())
Bedroom = Room("Bedroom", generate_items())

rooms = [Entryway, Kitchen, Living_room, Bathroom, Attic, Bedroom]

def find_item_by_name(name):
    for item in all_items:
        if item.name == name:
            return item
        
def find_room_by_name(name):
    for room in rooms:
        if room.name == name:
            return room

# Hahmonluontivalikko
def show_create_character_screen():
    print("Welcome to Trespass! Let's create your character.\n")

    given_name = input(("First, give your character a name:\n"))
    given_age = int(input("\nSpecify your characters age: "))
    given_gender = input("\nWhat is your characters gender?\nMale (1)\nFemale (2)\nOther (3)\nSelection: ")
    
    if(given_gender == "1" or given_gender.lower() == "male"):
        given_gender = "male"
    elif(given_gender == "2" or given_gender.lower() == "female"):
            given_gender = "female"
    elif(given_gender == "3" or given_gender.lower() == "other"):
            given_gender = "other"

    # Syöttää player-oliolle syötetyt arvot
    player.name = given_name
    player.age = given_age
    player.gender = given_gender

    print(f"Name: {player.name}, Age: {player.age}, Gender: {player.gender}")

    player_info_confirmation = input("Is this correct? (y/n)")
    if(player_info_confirmation == "y"):
        input("Character saved. Press enter to begin.")
    else:
        print("\n")
        show_create_character_screen()
    
# Tallentaa pelin tilan
def save_game_state():
     data_to_save = {
                 "saved_health": player.health,
                 "saved_inventory": player.inventory,
                 "saved_exp": player.exp,
                 "saved_level": player.level,
                 "saved_room": player.in_room.name,
                 "entryway_items": [item.name for item in Entryway.items]
              }

     with open("peliprojekti/save.json", "w") as save_file:
          json.dump(data_to_save, save_file)

# Lataa pelin tallennetun tilan
def load_saved_game_state():
    with open("peliprojekti/save.json", "r") as save_file:
        read_data = json.load(save_file)

    player.health, player.inventory, player.exp, player.level = read_data["saved_health"], read_data["saved_inventory"], read_data["saved_exp"], read_data["saved_level"]
    player.in_room = find_room_by_name(read_data["saved_room"])
    Entryway.items = [find_item_by_name(item_name) for item_name in read_data["entryway_items"]]

    print(f"Successfully loaded previous save with {player.inventory} in inventory, {player.exp} experience and player level {player.level}.")

def show_current_map():
    if(player.in_room == Entryway):
        print("""
    +-----------+     +----------+
    |  Bedroom  |-----| Bathroom |
    +-----------+     +----------+
           |
           |
    +-----------+     +----------+
    |   Attic   |-----| Kitchen  |
    +-----------+     +----------+
                         |
                         |
                    +----------+
                    |  Living  |
                    |   room   |
                    +----------+
                         |
                         |
                    +----------+
                    |*Entryway*|
                    +----------+
    """)
    elif(player.in_room == Living_room):
        print("""
+-----------+     +----------+
|  Bedroom  |-----| Bathroom |
+-----------+     +----------+
       |
       |
+-----------+     +----------+
|   Attic   |-----|  Kitchen |
+-----------+     +----------+
                     |
                     |
                +----------+
                | *Living  |
                |   room*  |
                +----------+
                     |
                     |
                +----------+
                | Entryway |
                +----------+
""")
    elif(player.in_room == Kitchen):
        print("""
    +-----------+     +----------+
    |  Bedroom  |-----| Bathroom |
    +-----------+     +----------+
           |
           |
    +-----------+     +-----------+
    |   Attic   |-----| *Kitchen* |
    +-----------+     +-----------+
                         |
                         |
                    +----------+
                    |  Living  |
                    |   room   |
                    +----------+
                         |
                         |
                    +----------+
                    | Entryway |
                    +----------+
    """)
    elif(player.in_room == Attic):
            print("""
    +-----------+     +----------+
    |  Bedroom  |-----| Bathroom |
    +-----------+     +----------+
           |
           |
    +-----------+     +----------+
    |  *Attic*  |-----|  Kitchen |
    +-----------+     +----------+
                         |
                         |
                    +----------+
                    |  Living  |
                    |   room   |
                    +----------+
                         |
                         |
                    +----------+
                    | Entryway |
                    +----------+
    """)
    elif(player.in_room == Bedroom):
            print("""
    +-----------+     +----------+
    | *Bedroom* |-----| Bathroom |
    +-----------+     +----------+
           |
           |
    +-----------+     +----------+
    |   Attic   |-----| Kitchen  |
    +-----------+     +----------+
                         |
                         |
                    +----------+
                    | *Living  |
                    |   room*  |
                    +----------+
                         |
                         |
                    +----------+
                    | Entryway |
                    +----------+
    """)
    elif(player.in_room == Bathroom):
            print("""
    +-----------+     +------------+
    |  Bedroom  |-----| *Bathroom* |
    +-----------+     +------------+
           |
           |
    +-----------+     +----------+
    |   Attic   |-----| Kitchen  |
    +-----------+     +----------+
                         |
                         |
                    +----------+
                    |  Living  |
                    |   room   |
                    +----------+
                         |
                         |
                    +----------+
                    | Entryway |
                    +----------+
    """)

def show_room_info():
    print(f"Current room: {player.in_room.name}\nItems in room:")
    for i in player.in_room.items:
        print(i.name, f"{i.value}$")

def select_next_room():
     if(player.in_room == Entryway):
        print(f"Current room: {player.in_roomname}\nItems in room:")
        
     selection = int(input("Which room to go in next?"))
     

# lukee save tiedoston, jos tyhjä, oleta, että pelaa ekaa kertaa
def start_game():
    with open("peliprojekti/save.json", "r") as save_file:
        if(not save_file.read(1)):
            show_create_character_screen()
            player.in_room = Entryway
        else:
            load_saved_game_state()

def main():
    start_game()

    while True:
       save_game_state()
       show_current_map()
       show_room_info()
       input()
        
main()


""" living_room = Room("Living Room", generate_items())

for i in living_room.items:
    print(i.name, f"{i.value}$") """

