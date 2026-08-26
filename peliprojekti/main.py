import sys

nimi = input("Anna nimesi: ")
ika = int(input("Anna ikäsi: "))

if(ika < 12):
    sys.exit("Sinun on oltava vähintään 12 vuotias, jotta voit pelata.")
else:
    print("Tervetuloa,", nimi + ",", ika)

while(True):
    print("(1) Syötä nimi uudelleen")
    print("(2) Syötä ikä uudelleen")
    print("(3) Lopeta")
    valinta = input("Valitse komento: ")
    if(valinta == "1" or valinta.lower() == "syötä nimi uudelleen"):
        nimi = input("Anna uusi nimi: ")
        print("Tervetuloa,", nimi)
        continue    
    elif(valinta == "2" or valinta.lower() == "syötä ikä uudelleen"):
        ika = int(input("Anna uusi ikä: "))
        if(ika < 12):
            sys.exit("Sinun on oltava vähintään 12 vuotias, jotta voit pelata.")
        else:
            print("Ikä", ika, "tallennettu")
            continue
    elif(valinta == "3" or valinta == "lopeta"):
        sys.exit()
    else:
        print("Virheellinen komento.")
        continue