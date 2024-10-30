# un diccionario esta compuesto por 2 elementos
# una LLAVE
# un VALOR
# 'Maradona':10

# dict(key,value),se puede usar cualquier tipo de datos
diccionario = {
    'IDE': 'integrated development Environment',
    'POO' : ' programacion orientada a objetos',
    'SABD': 'sistemas de administracion de base de datos'
}

# verificar la cantidad de elementos del diccionario
print(len(diccionario))

print(diccionario)

# acceder a un diccionario con la llave (key),cuidado con el tipeo
print(diccionario['IDE'])

# otra forma de recuperar un elemento
print(diccionario.get('POO'))
print(diccionario.get('SABD'))

# modificamos elementos
diccionario['IDE'] = 'entorno de desarrollo integrado'
print(diccionario)

# un diccionario puede modifcarse

# Como recorrer los elementos? a traves del bucle o ciclo for

for termino in diccionario:
    print(termino)
# para acceder al valor dentro de la
# la llave usamos una FUNCION ITEMS
# necesitamos una funcion para recorrer el diccionario
for termino, valor in diccionario.items():
    print(termino, valor)
#otras maneras de acceder a un diccionario
for termino, valor in diccionario.keys(): # usando funcion keys
    print(termino, valor)# muestra solo las llaves

for termino, valor in diccionario.values():# usamos una funciona para acceder al valor
    print(termino, valor)

# comprobar la existencia de algun elemento (si esta o no esta un elemento)
print('IDE' in diccionario) # devueleve ub booleano

# agregar un elemento
diccionario['PK'] = 'primary key'
print(diccionario)

# eliminar un elemento
diccionario.pop('SABD')
print(diccionario)

# vaciar o limpiar un diccionario
diccionario.clear()
print(diccionario)

# eliminar diccionario
del diccionario



