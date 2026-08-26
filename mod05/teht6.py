import random

nelion_sisalla = int(input("Anna arvottavien pisteiden määrä: "))
ympyran_sisalla = 0

i = 0

while(i < nelion_sisalla):
    piste_x = random.random()
    piste_y = random.random()
    if((piste_x * piste_x) + (piste_y * piste_y) < 1):
        ympyran_sisalla += 1
        i += 1
        continue
    else:
        i += 1
        continue

pi = 4 * ympyran_sisalla / nelion_sisalla

print(pi)
    


