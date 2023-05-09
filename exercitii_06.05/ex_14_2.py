# 14. #Varinata x
numar = int(input('Introduceti un numar pozitiv:'))
while numar <= 0:
    numar = int(input('Introduceti un numar pozitiv:'))

for i in range(numar+1):
    for j in range(i):
        print(i, end='')
    print()