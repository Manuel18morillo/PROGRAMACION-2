List = []

listElemt = ['Perro','Gato','Araña','Murcielago','Avion']

length = len(List)
print(length)

length = len(listElemt)
print(length)

IN = True,False
print(listElemt[0] + ' ' + listElemt[2] + ' ' + listElemt[4])


Datos_Personales = ['Manuel', '18' , '178cm' , 'Soltero' , 'adrees#222']
Datos_Personales.append('Estudiante')
print(Datos_Personales)


it_companies = ['Facebook', 'Google','Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.insert(0,'Tiktok')
print(it_companies)

IN = True,False
does_exist = 'Tiktok' in it_companies
print(does_exist)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

it_companies.pop(0)
print(it_companies)

del it_companies[2:3]
print(it_companies)

it_companies.clear()
print(it_companies)