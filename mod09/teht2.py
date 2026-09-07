class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnnus = rekisteritunnus
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


auto = Auto("ABC-123", 142)

print(f"Auton {auto.rekisteritunnnus} huippunopeus on {auto.huippunopeus}km/h, hetkellinen nopeus on {auto.nopeus}km/h, ja kuljettu matka on {auto.kuljettu_matka}km")

auto.kiihdyta(30)

print(f"Auton uusi nopeus on {auto.nopeus}km/h.")

auto.kiihdyta(70)

print(f"Auton uusi nopeus on {auto.nopeus}km/h.")

auto.kiihdyta(50)

print(f"Auton uusi nopeus on {auto.nopeus}km/h.")

auto.kiihdyta(-200)

print(f"Auton uusi nopeus on {auto.nopeus}km/h.")

