"""
7. Funcție fără return, primește un string și printează pe ecran:
Numărul de caractere lower case este x
Numărul de caractere upper case exte y

"""

a = str(input("Introduce a text:\n"))
def count_characters(a):
    uppercase = 0
    lowercase = 0
    for char in a:
        if char.islower():
            lowercase += 1
        elif char.isupper():
            uppercase += 1
        else:
            pass
    print(f"Uppecase letters nr. is:{uppercase}, lowercase letters nr. is: {lowercase}.")

count_characters(a)

