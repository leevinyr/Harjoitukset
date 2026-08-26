import random

luku = random.randint(1, 10)

while(True):
    arvaus = int(input("Arvaa luku 1-10: "))
    if(arvaus == luku):
        print("Oikein!")
        break
    elif(arvaus < luku):
        print("Liian pieni arvaus.")
        continue
    elif(arvaus > luku):
        print("Liian suuri arvaus.")
        continue