import sys

asema_koodit = []
asema_nimet = []

while(True):
    print("(1) Syötä uusi lentoasema")
    print("(2) Hae lentoasemaa")
    print("(3) Lopeta")

    valinta = int(input("Syötä valinta: "))

    if(valinta == 1):
        koodi = input("Syötä ICAO-koodi: ")
        nimi = input("Syötä aseman nimi: ")

        asema_koodit.append(koodi)
        asema_nimet.append(nimi)
        print("Asema tallennettu.")
        continue
    elif(valinta == 2):
        haku = input("Syötä aseman ICAO-koodi: ")
        print(asema_nimet[asema_koodit.index(haku)])
    elif(valinta == 3):
        sys.exit()
