"""
9. Printează cei 3 elevi și notele lor
Ex: ‘Ana a luat nota {x}’
Doar nota o vei lua folosindu-te de cheie

Pt data viitoare, varianta complexa

"""

dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
for keys, values in dict1.items():
#     print(f"Ana a luat nota: {dict1.get('Ana')}")
#     print(f"Gigel a luat nota: {dict1.get('Gigel')}")
#     print(f"Dorel a luat nota: {dict1.get('Dorel')}")
#     break
    print(f"{keys} a luat nota {values}")