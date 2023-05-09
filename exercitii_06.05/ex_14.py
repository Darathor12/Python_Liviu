zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
# Adaugă în zilele_sapt ‘luni’
# Afișează zile_sapt

print(zile_sapt)
print(type(zile_sapt))

if weekend.issubset(zile_sapt):
    print('Weekend este un subset al zilelor săptămânii')
else:
    print('Weekend nu este un subset al zilelor săptămânii')