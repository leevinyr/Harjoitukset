import random

while True:
    noppa1 = random.randint(1, 3)
    noppa2 = random.randint(1, 3)
    if(noppa1 == 3 and noppa2 == 3):
        print(f"Nyt tuli {noppa1} ja {noppa2}, jee!")
        break
    else:
        print(f"Nyt tuli {noppa1} ja {noppa2}, jatketaan")
