"""
4. Funcție care returnează aria dreptunghiului
"""


def dr_area(l1, l2):
    return l1 * l2


dr1 = dr_area(int(input("Introduce l1:\n")), int(input("Introduce l2:\n")))
print(f"Aria este:", dr1)
