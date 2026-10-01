import random
import os
import json
from classes import Entity, Player, Item, Room
from items import items

# game_active = False

player = Player("", 0, "")

# Generoi satunnaisen määrän item-olioita mahdollisia tavaroita sisältävästä listasta
def generate_items():
    room_items = []

    for i in range(0, random.randint(1, 4)):
        random_item = random.randint(0, len(items)-1)
        room_items.append(items[random_item])
        items.pop(random_item)

    return room_items

# Hahmonluontivalikko
def show_create_character_screen():
    print("Welcome to Trespass! Let's create your character.\n")

    given_name = input(("First, give your character a name:\n"))
    given_age = int(input("\nSpecify your characters age: "))

    given_gender = input("\nWhat is your characters gender?\nMale (1)\nFemale (2)\nOther (3)\nSelection: ")
    if(given_gender == 1 or given_gender.lower() == "male"):
        given_gender = "male"
    elif(given_gender == 2 or given_gender.lower() == "female"):
            given_gender = "female"
    elif(given_gender == 3 or given_gender.lower() == "other"):
            given_gender = "other"

    # Syöttää player-oliolle syötetyt arvot
    player.name = given_name
    player.age = given_age
    player.gender = given_gender

    input("Character saved. Press enter to begin.")

# Tallentaa pelin tilan
def save_game_state():
     data_to_save = {
                 "saved_health": player.health,
                 "saved_inventory": player.inventory,
                 "saved_exp": player.exp,
                 "saved_level": player.level,
                 "saved_room": player.in_room
              }

     with open("peliprojekti/save.json", "w") as save_file:
          json.dump(data_to_save, save_file)

# Lataa pelin tallennetun tilan
def load_saved_game_state():
    with open("peliprojekti/save.json", "r") as save_file:
        read_data = json.load(save_file)

    player.health, player.inventory, player.exp, player.level, player.in_room = read_data["saved_health"], read_data["saved_inventory"], read_data["saved_exp"], read_data["saved_level"], read_data["saved_room"],

    print(f"Successfully loaded previous save with {player.health}, {player.inventory}, {player.exp}, {player.level}")

# lukee save tiedoston, jos tyhjä, oleta, että pelaa ekaa kertaa
def start_game():
    # game_active = True

    with open("peliprojekti/save.json", "r") as save_file:
        if(not save_file.read(1)):
            show_create_character_screen()
        else:
            load_saved_game_state()

def main():
    start_game()

    while True:
        save_game_state()
        input("testi")
         
main()


""" living_room = Room("Living Room", generate_items())

for i in living_room.items:
    print(i.name, f"{i.value}$") """

