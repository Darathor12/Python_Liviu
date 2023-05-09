"""
12. Aceeași listă:

numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

Ordonează crescător lista fară să folosești sort.
Te poți inspira vizual de aici.
https://www.youtube.com/watch?v=lyZQPjUT5B4
"""
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#vom folosi 2 bucle pentru a compara fieacare element al listei cu celelte elemente

for x in range(len(numere)):
    for y in range(x+1, len(numere)):

# daca in lista gasim un element mai mic decat 'x' le interschimbam pozitiile.
# acest proces se va repeta pana cand lista este ordonata crescator
        if numere[y] < numere[x]:
            numere[x], numere[y] = numere[y], numere[x]
print(numere)


#varianta cu sort :
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]

numere.sort()

print(numere)