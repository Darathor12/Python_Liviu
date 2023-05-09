# 3.Aceeași listă:
# Vine un cumpărător care dorește să cumpere un Mercedes.
# Iterează prin ea prin modalitatea aleasă de tine.
# Dacă mașina e mercedes:
#    Printează ‘am găsit mașina dorită de dvs’
#    Ieși din ciclu folosind un cuvânt cheie care face acest lucru
# Altfel:
#    Printează ‘Am găsit mașina X. Mai căutam‘

"""
 for car in masini:
     if car == 'Mercedes':
         print('Am gasit masina dvs')
        break
     else:
        print(f' Am gasit masina {car}. Mai cautam')
"""
# 4.Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu excepția Trabant și Lăstun.
#
# Dacă mașina e Trabant sau Lăstun:
#    Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie else).
# Printează S-ar putea să vă placă mașina x.

"""
 for car in masini:
     if car in ['Trabant', 'Lastun']:
         continue
     print(f'S-ar putea sa va placa masina {car}')

"""
# 5.
#  Modernizează parcul de mașini:
#
# Crează o listă goală, masini_vechi.
# Iterează prin mașini.
# Când găsesti Lăstun sau Trabant:
# Salvează aceste mașini în masini_vechi.
# Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
# Printează Modele vechi: x.
# Modele noi: x.

"""

 masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
 masini_vechi = []
 
 for i in range(len(masini)):
     # if masini[i] in ['Lastun', 'Trabant']:
     if masini[i] == 'Lastun' or masini[i] == 'Trabant':
         masini_vechi.append(masini[i])
         masini[i] = 'Tesla'

 print(f'Modele vechi:', masini_vechi)
 print(f'Modele noi:', masini)