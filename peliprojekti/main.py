import random
from entity import Entity, Player, Item, Room
from items import items

def generate_items():
    room_items = []

    for i in range(0, random.randint(1, 4)):
        random_item = random.randint(0, len(items)-1)
        room_items.append(items[random_item])
        items.pop(random_item)

    return room_items

living_room = Room("Living Room", generate_items())

for i in living_room.items:
    print(i.name, f"{i.value}$")

