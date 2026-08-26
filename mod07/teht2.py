import random

luku = 0

valittu_luku = int(input("Anna nopan maksimisilmäluku: "))

def heita_noppaa(tahko):
    luku = random.randint(1, tahko)
    return luku

while(True):
    luku = heita_noppaa(valittu_luku)
    print(luku)
    if(luku == valittu_luku):
        break
    else:
        continue