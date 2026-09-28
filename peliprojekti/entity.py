import random

class Entity:
    def __init__(self, health):
        self.health = health

    def attack(self, target):
        if(self.level == 0):
            damage = random.randint(1, 20)
            target.health -= damage


class Player(Entity):
    def __init__(self, name, age, health):
        self.name = name
        self.age = age
        self.exp = 0
        self.level = 0
        self.inventory = []
        super().__init__(health)

    def collect(self, item):
        self.inventory.append(item)

    def gain_exp(self, amount):
        self.exp += amount
        
        if(self.exp >= 10):
            self.level = 1
        elif(self.exp >= 20):
            self.level = 2
        elif(self.exp >= 30):
            self.level = 3
        elif(self.exp >= 40):
            self.level = 4
        elif(self.exp >= 50):
            self.level = 5
        else:
            self.level = 0

class Room:
    def __init__(self, name, items):
        self.name = name
        self.items = items
                

class Item:
    def __init__(self, name, value):
        self.name = name
        self.value = value
