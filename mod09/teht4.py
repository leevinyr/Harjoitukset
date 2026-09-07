import random

autot = []

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, maara):
        if(maara < 0 and self.nopeus + maara > 0):
            self.nopeus += maara
        elif(maara < 0 and self.nopeus + maara < 0):
            self.nopeus = 0
        elif(maara >= 0 and self.nopeus + maara < self.huippunopeus):
            self.nopeus += maara
        elif(maara >= 0 and self.nopeus + maara > self.huippunopeus):
            self.nopeus = self.huippunopeus

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit

i = 0
while(i < 10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"
    autot.append(Auto(rekisteritunnus, huippunopeus))
    i += 1

def aloita_kilpailu(matka):
    kilpailu_kaynnissa = True
    while(kilpailu_kaynnissa):
        for i in autot:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)

            if(i.kuljettu_matka >= matka):
                print(f"Auto {i.rekisteritunnus} kulki ensimmäisenä yli {matka}km ja voitti!")
                kilpailu_kaynnissa = False
                break
            else:
                print(f"Auto {i.rekisteritunnus} on kulkenut {i.kuljettu_matka}km.")

                
aloita_kilpailu(1000)

for i in autot:
    print(f"Rekkari: {i.rekisteritunnus}, Huippunopeus: {i.huippunopeus}km/h, Nopeus: {i.nopeus}km/h, Kuljettu matka: {i.kuljettu_matka}km")
