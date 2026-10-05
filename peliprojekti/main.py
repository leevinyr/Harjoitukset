import random
import time
import json
import subprocess
import platform

from classes import Entity, Player, Item, Room
from items import all_items, available_items

player = Player("", 0, "")

Entryway = Room("Entryway", [])
Kitchen = Room("Kitchen", [])
Living_room = Room("Living room", [])
Bathroom = Room("Bathroom", [])
Attic = Room("Attic", [])
Bedroom = Room("Bedroom", [])

controls_text = "Controls: \nCollect item: 1, Discard item: 2, Change room: 3"

# Generoi satunnaisen määrän item-olioita mahdollisia tavaroita sisältävästä listasta
def generate_items():
    room_items = []

    for i in range(0, random.randint(1, 4)):
        random_item = random.randint(0, len(available_items)-1)
        room_items.append(available_items[random_item])
        available_items.pop(random_item)

    return room_items

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
    given_name = input(("Give your character a name:\n"))
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
                 "player_name": player.name,
                 "player_age": player.age,
                 "player_gender": player.gender,
                 "saved_health": player.health,
                 "saved_inventory": [item.name for item in player.inventory],
                 "saved_exp": player.exp,
                 "saved_level": player.level,
                 "saved_room": player.in_room.name,
                 
                 "entryway_items": [item.name for item in Entryway.items],
                 "living_room_items": [item.name for item in Living_room.items],
                 "kitchen_items": [item.name for item in Kitchen.items],
                 "attic_items": [item.name for item in Attic.items],
                 "bedroom_items": [item.name for item in Bedroom.items],
                 "bathroom_items": [item.name for item in Bathroom.items],
              }

     with open("peliprojekti/save.json", "w") as save_file:
          json.dump(data_to_save, save_file)

# Lataa pelin tallennetun tilan
def load_saved_game_state():
    with open("peliprojekti/save.json", "r") as save_file:
        read_data = json.load(save_file)

    player.name, player.age, player.gender, player.health, player.exp, player.level = read_data["player_name"], read_data["player_age"], read_data["player_gender"], read_data["saved_health"], read_data["saved_exp"], read_data["saved_level"]
    player.in_room = find_room_by_name(read_data["saved_room"])
    player.inventory = [find_item_by_name(item_name) for item_name in read_data["saved_inventory"]]
    Entryway.items = [find_item_by_name(item_name) for item_name in read_data["entryway_items"]]
    Living_room.items = [find_item_by_name(item_name) for item_name in read_data["living_room_items"]]
    Kitchen.items = [find_item_by_name(item_name) for item_name in read_data["kitchen_items"]]
    Attic.items = [find_item_by_name(item_name) for item_name in read_data["attic_items"]]
    Bedroom.items = [find_item_by_name(item_name) for item_name in read_data["bedroom_items"]]
    Bathroom.items = [find_item_by_name(item_name) for item_name in read_data["bathroom_items"]]

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
                    |*ENTRYWAY*|
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
                | *LIVING  |
                |   ROOM*  |
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
    |   Attic   |-----| *KITCHEN* |
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
    |  *ATTIC*  |-----|  Kitchen |
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
    | *BEDROOM* |-----| Bathroom |
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
                    | Entryway |
                    +----------+
    """)
    elif(player.in_room == Bathroom):
            print("""
    +-----------+     +------------+
    |  Bedroom  |-----| *BATHROOM* |
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
        print(f"{player.in_room.items.index(i)} {i.name}, {i.value}$")

def select_item_collect():
     selection = int(input("Select item to collect: "))
     if(selection >= 0 and selection < len(player.in_room.items)):
        player.collect_item(player.in_room.items[selection])
     else:
        print("Invalid selection.")
        time.sleep(1)

def select_item_discard():
     player.show_inventory()

     selection = input("Select an item to discard: ")
     if(selection == "" or int(selection) < 0 or int(selection) > len(player.inventory) - 1):
          print("Invalid selection.")
          time.sleep(1)
     else:
          player.discard_item(player.inventory[int(selection)])
     
def select_room_change():
     print("Nearby rooms: ")
     if(player.in_room == Entryway):
          print("1 Living room")
     elif(player.in_room == Living_room):
          print("1 Kitchen\n2 Entryway")
     elif(player.in_room == Kitchen):
              print("1 Attic\n2 Living room")
     elif(player.in_room == Attic):
              print("1 Bedroom\n2 Kitchen")
     elif(player.in_room == Bedroom):
              print("1 Bathroom\n2 Attic")
     elif(player.in_room == Bathroom):
              print("1 Bedroom")
    
     selection = int(input("Select next room: "))
     if(player.in_room == Entryway and selection == 1):
          player.in_room = Living_room
     elif(player.in_room == Living_room and selection == 1):
          player.in_room = Kitchen
     elif(player.in_room == Living_room and selection == 2):
              player.in_room = Entryway
     elif(player.in_room == Kitchen and selection == 1):
              player.in_room = Attic
     elif(player.in_room == Kitchen and selection == 2):
              player.in_room = Living_room
     elif(player.in_room == Attic and selection == 1):
              player.in_room = Bedroom
     elif(player.in_room == Attic and selection == 2):
              player.in_room = Kitchen
     elif(player.in_room == Bedroom and selection == 1):
              player.in_room = Bathroom
     elif(player.in_room == Bedroom and selection == 2):
              player.in_room = Attic
     elif(player.in_room == Bathroom and selection == 1):
              player.in_room = Bedroom
     else:
           print("Invalid selection.")
           time.sleep(1)
     
def ask_next_command():
     command = int(input("Enter command: "))
     if(command == 1):
          select_item_collect()
     elif(command == 2):
          select_item_discard()
     elif(command == 3):
          select_room_change()
     else:
          print("Invalid selection.")
          time.sleep(1)

# lukee save tiedoston, jos tyhjä, oleta, että pelaa ekaa kertaa
def start_game():
    with open("peliprojekti/save.json", "r") as save_file:
        if(not save_file.read(1)):
            Entryway.items = generate_items()
            Living_room.items = generate_items()
            Kitchen.items = generate_items()
            Attic.items = generate_items()
            Bedroom.items = generate_items()
            Bathroom.items = generate_items()

            player.in_room = Entryway

            with open("peliprojekti/intro.txt", "r") as f:
                 for line in f:
                      print(line)
                      time.sleep(2)
                 print("\n")

            show_create_character_screen()
        else:
            load_saved_game_state()

def clear_screen():
    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:
        subprocess.run(["clear"], shell=True)

def main():
    start_game()

    while True:
       clear_screen()
       save_game_state()
       print(controls_text)
       show_current_map()
       show_room_info()
       ask_next_command()
        
main()
