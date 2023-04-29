"""
7. Citește de la tastatură:
lungimea;
lățimea.
   Afișează: 'Aria dreptunghiului este x'.

"""

#in loc de int putem folosi float sau putem declara variabilele direct.

latime = int(input("Afiseaza latimea:"))
lungime = int(input("afiseaza lungimea:"))

print(f"aria dreptunghiului este: {lungime * latime}")
