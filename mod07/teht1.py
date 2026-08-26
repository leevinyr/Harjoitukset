import random

luku = 0

def heita_noppaa():
    luku = random.randint(1, 6)
    return luku

while(True):
    luku = heita_noppaa()
    print(luku)
    if(luku == 6):
        break
    else:
        continue