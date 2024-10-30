# set:no es completamente mutable ni inmutable,no mantienen ningun indice,no tiene
# un elemento tipo set

# tipo set
planetas = {'marte','júpiter','venus'}
print(len(planetas)) # usamos la funcion len = length significa largo

#funciones a usar con lent

# revisar si un elemento existe dentro de set
print('martes' in planetas)
## revisar si un elemento NO existe dentro de set
print('martes'not in planetas) #false

#agregar otro elemento
planetas.add('tierra') # add es una funcion
print(planetas)

#se usan SET para datos no duplicados como dni,matriculas etc

# eliminar elementos ,puede arrojar un error si el elemento no existe
planetas.remove('jupiter')
print(planetas)
planetas.discard('Tierra')
print(planetas)

# discard y remove son diferentes

# limpiar el set o conjunto

planetas.clear()
print(planetas)

#repaso de set o conjunto de elementos desordendados,son unicos y admite cualquier tipo de datos

# para definir un conjunto
conjunto2 = set()
conjunto1 = {'bye','4'}
conjunto2.add(7)
conjunto2.add('Hola')
print(conjunto2)
conjunto1.add('Hola')
print(conjunto1)
print(3 not in conjunto1) # preguntamos si el numero 3 NO esta en el conjunto1

# como hacer igualdad en dos conjuntos
print(conjunto1 == conjunto2) # nos devuelve como respuesta un bool

#operaciones de conjunto
conjunto3 = conjunto1 | conjunto2 #la linea une los dos conjuntos
conjunto3 = conjunto1 & conjunto2 # que elementos tienen en comun
print(conjunto3)

conjunto3 = conjunto1 - conjunto2 # asigna el valor que esta en el conjunto1 y no en el conjunto2
print(conjunto3)

conjunto3 = conjunto1 ^ conjunto2 # elementos que no se comparten o que son diferentes entre ambos
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # aqui preguntamos si un conjunto es un subconjunto de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1))
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))

# como saber si ambos son disconxos,esto es si no comparten eleentos en comun

print(conjunto1.isdisjoint(conjunto2)) # no hay cosas en cmun

#convertir un conjunto totalmente en inmutable
conjunto1 = frozenset # esto hace que el conjunto sea totlmente INMUTABLE
#NO se puede agregar,modificar ni eliminar elementos del conjunto
