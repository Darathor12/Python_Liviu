"""
18. Același string.
Salvează într-o variabilă și afișează indexul de start al cuvântului rock (hint: este o funcție care te ajuta sa faci asta)
Folosind această variabilă + slicing, afișează tot stringul până la acest cuvânt
output: 'Coral is either the stupidest animal or the smartest'
Initial string: 'Coral is either the stupidest animal or the smartest rock'
"""

s = 'Coral is either the stupidest animal or the smartest rock'
r = s.find("rock")
print(r)

# print(f"Stringul rezultat este {s[0:s.find('rock')]}")

print(f"Stringul rezultat este {s[0:r]}")