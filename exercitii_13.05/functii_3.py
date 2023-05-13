"""
3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)

"""

def get_number_char(name):
    return (len(name))
name = str(input("Introduce name:"))
space = name.count(" ")
print(f'Total nr. of characters is: {get_number_char(name)-space}')
