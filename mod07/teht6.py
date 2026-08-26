import math

def laske_hinta(halkaisija, hinta):
    pinta_ala = (math.pi * (halkaisija/2) ** 2) / 10000
    hinta_per_m2 = hinta / pinta_ala

    return hinta_per_m2

halkaisija = float(input("Anna pyöreän pizzan halkaisija senttimetreinä: "))
hinta = float(input("Anna pizzan hinta euroina: "))

print(f"Pizzan hinta on: {laske_hinta(halkaisija, hinta): .2f}€/m^2")
