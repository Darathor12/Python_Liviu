"""
13. Exercițiu:
citește un string de la tastatură (ex: alabala portocala);
salvează primul caracter într-o variabilă - indiferent care este el, încearcă cu 2 stringuri diferite;
capitalizează acest caracter peste tot, mai puțin pentru primul și ultimul caracter => alAbAlA portocAla.

"""

tastatura = input("scrie un string:\n")

x = tastatura[0]
# print(x)
y = tastatura.replace(x,x.upper())
print(y)
print(y[0].replace(y[0],y[0].lower())+y[1:-1]+y[-1].replace(y[-1],y[-1].lower()))

# print(tastatura)
# print(len(tastatura))
