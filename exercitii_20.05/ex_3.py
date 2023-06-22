"""
3. Clasa Angajat
     Atribute: nume, prenume, salariu
     Constructor pentru toate atributele
     Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""

class Angajat:
    def init(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descrie(self):
        return f'Angajatul {self.nume} {self.prenume} are salariul {self.salariu}'

    def nume_complet(self):
        return f'Nume complet este {self.nume} {self.prenume}'

    def salariu_lunar(self):
        return f'Salariul este de {self.salariu} lei'

    def salariu_anual(self):
        return f'Salariu anual este de {self.salariu * 12}'

    def marire_salariu(self, procent):
        if procent < 0:
            return f'Salariul s-a micsorat, noul salariul este {self.salariu * (1 + procent/100)}'
        elif procent == 0:
            return f'Salariul a ramas la fel: {self.salariu}'
        else:
            return f'Dupa marirea de {procent}%, salariul este {self.salariu * (1 + procent/100)}'

angajat1 = Angajat('Popescu', 'Ion', 2000)
print(angajat1.descrie())
print(angajat1.nume_complet())
print(angajat1.salariu_lunar())
print(angajat1.salariu_anual())
print(angajat1.marire_salariu(-20))
print(angajat1.marire_salariu(0))
print(angajat1.marire_salariu(20))