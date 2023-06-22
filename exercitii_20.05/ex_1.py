"""
1.Clasa Cerc
    Atribute: rază, culoare
    Constructor pentru ambele atribute
    Metode:
descrie_cerc() - va PRINTA culoarea și raza
aria() - va RETURNA aria
diametru()
circumferinta()

"""

class Cerc:
    def __init__(self, r, color, pi):
        self.r = r
        self.color = color
        self.pi = 3.14

    def descrie_cerc(self):
        print(f"Cercul are culoarea {self.color} si raza {self.r}")

    def aria(self):
        return self.pi*(self.r**2)

    def diametru(self):
        return 2*self.r

    def circumferinta(self):
        return 2*self.pi*self.r

c1 = Cerc(5, "galben", 3.14)
c1.descrie_cerc()
print(c1.aria())
print(c1.diametru())
print(c1.circumferinta())

print(f"Aria este {c1.aria()}, diametrul este {c1.diametru()} si circumferinta este {c1.circumferinta()}.")
print("Aria este:", c1.aria(), "Diametrul este:", c1.diametru(), "Circumferinta este:", c1.circumferinta())