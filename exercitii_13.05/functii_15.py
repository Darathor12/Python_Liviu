"""
15. Funcție care să primească un număr și să returneze suma tuturor numerelor de la 0 la acel număr.
Exemplu: dacă dăm numărul 3, suma va fi 6 (0+1+2+3)

"""

n = int(input("Introduce a number, program will compute the sum of all numbers up to and including the number you provide:\n"))

#Var1
def compute_sum(n):
    suma = 0
    for num in range(1, n+1):
        suma = suma + num
    print(f"The sum of the numbers is:{suma}")

compute_sum(n)

#Var2
def compute_sum2(n):
    return f"{n*(n+1)/2:.0f}" # .0f pt a nu avea nici o zecimala

print(compute_sum2(n))

