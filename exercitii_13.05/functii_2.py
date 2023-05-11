# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def check_positive(a):
    if a >= 0:
        # print("The number you introduced is positive!")
        print(a.ispositive())
    else:
        # print("The number you introduced is negative")
        print(a.ispositive())

check_positive(float(input("Introduce a number to check its parity:\n")))
