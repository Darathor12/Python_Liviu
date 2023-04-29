"""
11. Exercițiu:
citește de la tastatură un string de dimensiune impară;
afișează caracterul din mijloc.
"""

inp_string = str(input("introdu un string impar, minim 3 caractere:\n"))
# if len(inp_string) < 3:
#     print("ai introdus mai putin de 3 caractere")
# elif (len(inp_string) % 2) == 0:
#     print("numarul caracterelor introduse este par, te rog introdu un string impar!")
print(len(inp_string))
print(len(inp_string) // 2)

print(inp_string[len(inp_string) // 2])         #intre paranteze patrate este index-ul.