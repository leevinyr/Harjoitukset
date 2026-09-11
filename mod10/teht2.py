class Hissi:
    def __init__(self, alin_kerros, ylin_kerros, nimi):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nimi = nimi

        self.kerros = 0

    def kerros_ylos(self):
        self.kerros += 1
        print(f"Hissi on kerroksessa {self.kerros}")

    def kerros_alas(self):
        self.kerros -= 1
        print(f"Hissi on kerroksessa {self.kerros}")

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
            self.hissit.append(Hissi(alin_kerros, ylin_kerros, f"hissi{i}"))
            i += 1

    def aja_hissia(self, numero, kohdekerros):
        self.hissit[numero].siirry_kerrokseen(kohdekerros)
