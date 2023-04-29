"""
12. Ne imaginăm o echipă de fotbal pt teren sintetic.
3 Schimbări maxime admise:

Declară o Listă cu 5 jucători
Schimbari_efectuate = te joci tu cu valori diferite
Schimbari_max = 3

Dacă Jucătorul x e în teren și mai avem schimbări la dispoziție
Efectuează schimbarea
Șterge jucătorul scos din listă
Adaugă jucătorul intrat
Afișază a intrat x, a ieșit y, mai ai z schimbări

Dacă jucătorul nu e în teren:
Afișază ‘nu se poate efectua schimbarea deoarece jucătorul x nu e în teren’
Afișază ‘mai ai z schimbări’

Testează codul cu diferite valori

Google search hint
“how to check if item is în list python”

"""

Jucatori = ['Alexandru', 'Ion', 'Popa', 'Dorel', 'Gigel']
Rezerve = ['Liviu', 'Marius', 'Grigore']
schimbari_efectuate = 0
schimbari_max = 3
# schimbari_ramase = schimbari_max - schimbari_efectuate
# print(schimbari_ramase)
# nume_jucator = str(input("Introdu numele jucatorului care ar trebui schimbat:\n"))
while schimbari_efectuate < schimbari_max:
    nume_jucator = str(input("Introdu numele jucatorului care ar trebui schimbat:\n"))
    schimbari_ramase = schimbari_max - schimbari_efectuate
    if nume_jucator in Jucatori:
        Jucatori.remove(nume_jucator)
        Jucatori.append(Rezerve[0])
        schimbari_efectuate += 1
        schimbari_ramase = schimbari_max - schimbari_efectuate
        print(f"A iesit {nume_jucator}, a intrat {Rezerve[0]}, mai sunt {schimbari_ramase} schimbari ramase.")
        print(f"Echipa din teren este {Jucatori}")
        Rezerve.pop(0)
    # elif schimbari_efectuate == schimbari_max:
    #     print("Nu se mai pot efectua schimbari.")
    else:
        print(f"Jucatorul nu este in teren, mai sunt {schimbari_ramase} schimbari ramase.")