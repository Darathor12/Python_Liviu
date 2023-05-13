# 2. Funcție care să returneze TRUE dacă un număr este par, FALSE pentru impar

def check_positive(a):
    if a > 0:
        # print("The number you introduced is positive!")
        print(True)
    elif a < 0:
        # print("The number you introduced is negative")
        print(False)
    else:
        print("Number is 0")

check_positive(float(input("Introduce a number to check its value:\n")))
