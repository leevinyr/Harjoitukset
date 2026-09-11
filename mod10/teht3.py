class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, nimi):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nimi = nimi

        self.kerros = 0

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi {self.nimi} on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi {self.nimi} on kerroksessa {self.kerros}")

    def siirry_kerrokseen(self, uusi_kerros):
        while(self.kerros != uusi_kerros):
            if(self.kerros < uusi_kerros):
                self.kerros_ylos()
            elif(self.kerros > uusi_kerros):
                self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_maara):
        self.hissit = []
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.hissien_maara = hissien_maara

        i = 0
        while(i < self.hissien_maara):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros, i))
            i += 1

    def aja_hissia(self, nimi, kohdekerros):
        self.hissit[nimi].siirry_kerrokseen(kohdekerros)

    def palohalytys(self):
        print("Palohälytys! Ajetaan kaikki hissit pohjakerrokseen.")
        for i in self.hissit:
            self.aja_hissia(i.nimi, 0)

talo1 = Talo(0, 10, 4)

talo1.aja_hissia(1, 3)
talo1.aja_hissia(2, 6)
talo1.aja_hissia(3, 8)
talo1.aja_hissia(0, 4)

talo1.palohalytys()
