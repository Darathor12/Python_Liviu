"""
20.  Citește de la tastatură un string
Verifică dacă primul și ultimul caracter sunt la fel. Se va folosi un assert
Atenție: se dorește ca programul să fie case insensitive - 'apA' e acceptat

"""

s = str(input("Introdu string-ul:\n"))
print(s)
assert s[0].lower() == s[-1].lower()

