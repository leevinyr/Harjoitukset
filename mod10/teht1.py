class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros

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

h = Hissi(0, 10)

h.siirry_kerrokseen(9)

h.siirry_kerrokseen(h.alin_kerros)