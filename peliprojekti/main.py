import sys

inventory = []

def change_name():
    name = input("Anna nimesi: ")
    return name

def change_age():
    age = int(input("Anna ikäsi: "))
    if(age < 12):
        sys.exit("Sinun on oltava vähintään 12 vuotias, jotta voit pelata.")
    else:
        return age

def add_to_inv():
    while(True):
        asia = input("Lisää asia inventoryan (tyhjä lopettaa): ")
        if(asia == ""):
            break
        else:
            inventory.append(asia)

def show_inventory():
    for i in inventory:
        print(i)

def exit():
    sys.exit()

change_name()
change_age()







""" 
while(True):
    print("(1) Syötä name uudelleen")
    print("(2) Syötä ikä uudelleen")
    print("(3) Lisää asioita inventoryan")
    print("(4) Näytä inventory")
    print("(0) Lopeta")

    valinta = input("Valitse komento: ")

    if(valinta == "1" or valinta.lower() == "syötä name uudelleen"):
        print(f"Tervetuloa, {change_name()}")
        continue    
    elif(valinta == "2" or valinta.lower() == "syötä ikä uudelleen"):
        print(f"Ikä {change_age()} tallennettu.")
        continue
    elif(valinta == "3" or valinta.lower() == "lisää asioita inventoryan"):
        add_to_inv()
    elif(valinta == "4" or valinta.lower() == "näytä inventory"):
        show_inventory()
    elif(valinta == "0" or valinta == "lopeta"):
        exit()
    else:
        print("Virheellinen komento.")
        continue """