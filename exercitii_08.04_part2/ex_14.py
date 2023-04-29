"""
14.Folosește un if și verifică dacă:
Weekend este un subset al zilelor din săptămânii.
Weekend nu este un subset al zilelor din săptămânii.

"""
zile_sapt = {'luni', 'marți', 'miercuri', 'joi', 'vineri', 'sâmbăta', 'duminică'}
weekend = {'sâmbăta', 'duminică'}
if weekend.issubset(zile_sapt):
    print("Setul weekend este un subset al setului zile_sapt")
else:
    print("Setul weekend nu este un subset al setului zile_sapt")