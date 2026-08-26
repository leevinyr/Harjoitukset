import random

maara = int(input("Anna arpakuutioiden määrä: "))

summa = 0
for i in range(0, maara, 1):
    luku = random.randint(1, 6)
    summa += luku

print("Arpakuutioiden silmälukujen summa:", summa)