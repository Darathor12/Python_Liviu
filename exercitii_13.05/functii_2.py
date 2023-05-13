# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def is_even(a):
    if a % 2 == 0:
        print(True)
    else:
        print(False)

is_even(float(input("Introduce a number to check its parity:\n")))
