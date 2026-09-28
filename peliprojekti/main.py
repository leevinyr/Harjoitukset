import random
import os
from classes import Entity, Player, Item, Room
from items import items

game_active = False

# Generates a random amount of items into a room from a list of available items
def generate_items():
    room_items = []

    for i in range(0, random.randint(1, 4)):
        random_item = random.randint(0, len(items)-1)
        room_items.append(items[random_item])
        items.pop(random_item)

    return room_items

# lukee save tiedoston, jos tyhjä, oleta, että pelaa ekaa kertaa
def start_game():
    with open("save.json", "r") as save_file:
        if(os.stat(save_file).st_size == 0):
            print("Welcome to Trespass! Let's create your character.")

def main():
    while game_active:
        print()

start_game()


""" living_room = Room("Living Room", generate_items())

for i in living_room.items:
    print(i.name, f"{i.value}$") """

