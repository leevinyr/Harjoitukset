nimet = ()

while(True):
    nimi = input("Anna nimi: ")
    if(nimi == ""):
        break
    elif(nimi in nimet):
        print("Aiemmin syötetty nimi.")
    else:
        print("Uusi nimi.")
        nimet = nimet + (nimi,)
    continue

for i in nimet:
    print(i)