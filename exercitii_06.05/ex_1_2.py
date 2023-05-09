Ex 1 si 2 Cicluri Repetitive """
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']

Folosește un for că să iterezi prin toată lista și să afișezi;
●    ‘Mașina mea preferată este x’. -> lungime, range
●    Fă același lucru cu un for each.
●    Fă același lucru cu un while.
"""


#cazul simplu doar cu for
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#l=len(masini)
#for i in range(l): #range(l)=9
 #   print(masini[i])


#cazul cu for each ->tine cont de indexul fiecarui element
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
#for i in masini:
 # print(f'Masina mea preferata este: {i}')


#i=0 #in functie de index
#while i< len(masini):
 #   print(f'Masina mea preferata este: {masini[i]}')
  #  i+=1

#2
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
res =[]
#for i in masini:
#    x = i[0].upper() + i[1:-1] + i[-1].upper()
#    res.append(x)
#res = " ".join(res)
#print("String after:", res)

#Var 1
#l=len(masini)
#res.append(masini[0])
#for i in range(1,l-1,1):
   # x = masini[i].upper()
 #   res.append(x)
#res.append(masini[l-1])
#print(res)

#var 2
for i in range(1,len(masini)-1):
    masini[i] = masini[i].upper()
print(masini)