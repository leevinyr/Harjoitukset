pienin = None
suurin = None

while(True):
    syote = input("Anna luku (tyhjä: lopeta): ")

    if(syote == ""):
        break

    luku = float(syote)
    if(pienin is None or luku < pienin):
        pienin = luku
        continue
    elif(suurin is None or luku > suurin):
        suurin = luku
        continue

print("Suurin annettu luku:", suurin)
print("Pienin annettu luku:", pienin)