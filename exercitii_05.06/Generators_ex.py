"""
Implementați un generator pentru loteria 6/49 și noroc:
Primele 6 apelări către generator vor da cate un numar intre 1 si 49 (inclusiv
Ultima apelare va da un singur număr de “noroc” format din 7 cifre
"""
def loto_gen():
    my_list = random.sample(range(1,50),6)
    for nr in my_list:
        yield nr
    yield random.randint(1_000_000, 9_999_999)

for nr in loto_gen():
    print(nr)