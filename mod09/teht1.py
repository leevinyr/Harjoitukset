class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.kuljettu_matka = 0

auto = Auto("ABC-123", 142)

print(f"Auton {auto.rekisteritunnnus} huippunopeus on {auto.huippunopeus}, hetkellinen nopeus on {auto.hetkellinen_nopeus}, ja kuljettu matka on {auto.kuljettu_matka}")