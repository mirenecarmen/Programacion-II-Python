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



