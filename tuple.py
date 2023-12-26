#list[1,2,3]

#tuple = (1, 'iki',3)

#print(type(list))
#print(type(tuple))

#print(len(tuple))
#print(len(list))


list=[ 'ali', 'veli']
tuple=('damlar','ayşe','ayşe')
names= ('damla','erva', 'ayşe') + tuple
#mesela listedeki aliyi ahmet ile değiştirmek istediğimizde list[0]= 'Ahmet' yazar ve atarız 
#ama list ve tuple calısma mantıgı aynı olsa da tuple a list e atayıp değiştirildiği gibi tuple içeriği sonradan değiştirilemez
list[0]='Ahmet'
print(tuple.count('ayşe'))
print(names)
print(list)
print(tuple)