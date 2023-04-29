"""
6. Citește de la tastatură:
numele;
prenumele.
    Afișează: 'Numele complet are x caractere'.

"""

nume = str(input("Introdu numele:\n"))
prenume = str(input("Introdu prenumele:\n"))
nrcaract = len(nume)+len(prenume)
print(f"Numele complet are {nrcaract} caractere.")
print(f"Numele complet are: {len(nume+prenume)} caractere")
