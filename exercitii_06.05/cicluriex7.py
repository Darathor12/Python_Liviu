"""
7. Având lista:
numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
Iterează prin ea.
Afișează de câte ori apare 3 (nu ai voie să folosești count).
"""

numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] # lista de variabile
numara = 0 # am definit variabila 'numara' pentru a numara de cateva ori va aparea 3 in lista mea
for numar in numere:
# interam fiecare element din lista ,pt fiecare element verificam daca egal cu 3
#daca este egal cu 3 crestem valaorea variabilei "numara" cu +1
    if numar == 3:
        numara+=1
# printam de cate ori apare 3 in lista noastra.
print(f'NUmarul 3 apare de {numara} ori in lista mea.' )



#varianta cu count :
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#
# numara = numere.count(3)
# print(f'NUmarul 3 apare de {numara} ori in lista mea' )
