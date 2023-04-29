"""
14.Exercițiu:
citește un user de la tastatură;
citește o parolă;
afișează: 'Parola pt user x este ***** și are x caractere';
***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie să afișeze corect.

eg: parola abc => ***
      parola abcd => ****

"""

user = input("introdu user:\n")
parola = input('introdu parola:\n')
lungime_parola = len(parola)
indicator = '*' * lungime_parola
print(f"parola pt user {user} este {indicator} si are {lungime_parola} caractere") #var
print(f"parola pt user {user} este {parola.replace(parola, 'x' * len(parola))} si are {len(parola) caractere}")

