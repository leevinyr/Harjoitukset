import sys

ostoslista = []

def muuta_nimi():
    nimi = input("Anna nimesi: ")
    return nimi

def muuta_ika():
    ika = int(input("Anna ikäsi: "))
    if(ika < 12):
        sys.exit("Sinun on oltava vähintään 12 vuotias, jotta voit pelata.")
    else:
        return ika

def lisaa_ostoslistaan():
    while(True):
        asia = input("Lisää asia ostoslistaan (tyhjä lopettaa): ")
        if(asia == ""):
            break
        else:
            ostoslista.append(asia)

def nayta_ostoslista():
    for i in ostoslista:
        print(i)

def lopeta():
    sys.exit()

muuta_nimi()
muuta_ika()

while(True):
    print("(1) Syötä nimi uudelleen")
    print("(2) Syötä ikä uudelleen")
    print("(3) Lisää asioita ostoslistaan")
    print("(4) Näytä ostoslista")
    print("(0) Lopeta")

    valinta = input("Valitse komento: ")

    if(valinta == "1" or valinta.lower() == "syötä nimi uudelleen"):
        print(f"Tervetuloa, {muuta_nimi()}")
        continue    
    elif(valinta == "2" or valinta.lower() == "syötä ikä uudelleen"):
        print(f"Ikä {muuta_ika()} tallennettu.")
        continue
    elif(valinta == "3" or valinta.lower() == "lisää asioita ostoslistaan"):
        lisaa_ostoslistaan()
    elif(valinta == "4" or valinta.lower() == "näytä ostoslista"):
        nayta_ostoslista()
    elif(valinta == "0" or valinta == "lopeta"):
        lopeta()
    else:
        print("Virheellinen komento.")
        continue