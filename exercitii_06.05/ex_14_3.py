# S2/Part2/Ex14 - alte variante
numar = input("Introdu un numar: ")
numar = int(numar)

for i in range(numar+1):
    for j in range(i):
        print(i, end=" ")
    print()

i = 1
while i <= numar:
    for j in range(i):
        print(i, end=" ")
    print()
    i += 1

for i in range(numar+1):
    print((str(i)+" ")*i)