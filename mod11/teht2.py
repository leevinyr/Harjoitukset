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

class Kilpailu:
    def __init__(self, kilpailun_nimi, kilpailun_pituus, autolista):
        self.kilpailun_nimi = kilpailun_nimi
        self.kilpailun_pituus = kilpailun_pituus
        self.autolista = autolista
        self.kilpailu_kaynnissa = True
        self.kuluneet_tunnit = 0

    def kilpailu_ohi(self):
        for i in self.autolista:
            if(i.kuljettu_matka >= self.kilpailun_pituus):
                print(f"Auto {i.rekisteritunnus} voitti!")
                self.kilpailu_kaynnissa = False
                return True
            else:
                return False
    
    def tunti_kuluu(self):
        for i in self.autolista:
            i.kiihdyta(random.randint(-10, 15))
            i.kulje(1)
        
        self.kuluneet_tunnit += 1

    def tulosta_tilanne(self):
        for i in autot:
            print(f"Rekkari: {i.rekisteritunnus}, Huippunopeus: {i.huippunopeus}km/h, Nopeus: {i.nopeus}km/h, Kuljettu matka: {i.kuljettu_matka}km")
        
i = 0
while(i < 10):
    huippunopeus = random.randint(100, 200)
    rekisteritunnus = f"ABC-{i}"
    autot.append(Auto(rekisteritunnus, huippunopeus))
    i += 1

kilpailu1 = Kilpailu("Suuri romuralli", 8000, autot)

while(kilpailu1.kilpailu_kaynnissa):
    kilpailu1.tunti_kuluu()
    if(kilpailu1.kilpailu_ohi() and kilpailu1.kuluneet_tunnit % 10 != 0):
        kilpailu1.tulosta_tilanne()
        break
    elif(kilpailu1.kilpailu_ohi() and kilpailu1.kuluneet_tunnit % 10 == 0):
        kilpailu1.tulosta_tilanne()
        print(f"Tunti {kilpailu1.kuluneet_tunnit}: ")
        break
    elif(kilpailu1.kilpailu_ohi() == False and kilpailu1.kuluneet_tunnit % 10 == 0):
        print(f"Tunti {kilpailu1.kuluneet_tunnit}: ")
        kilpailu1.tulosta_tilanne()
    else:
        continue
