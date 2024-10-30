 # definimos una tupla

 cocina = ("cuchara","cuchillo","tenedor")
 print(len(cocina))

 # acceder a un elemento, para esto utilizamos corchetes no parentesis

print(cocina[0])

#mostrar de manera inversa
print(cocina[-1])

# accedeer a un rango
print(cocina[0:1])

# ejemplo
verduras = ("papa",) # una tupla necesita aunque sea un elemento y la coma

# de lo contrario solo seria un tipo str o cadena

for cocinar in cocina:
    print(cocinar,end="") # print esta usando barra invertida para saltos de lina

cocinaLista = -list(cocina)
cocinaLista[0] = "Plato"
cocina = tuple(cocinaLista)
print("\n",cocina)

# del cocina
# print(cocina)

# diferencia entre lista y tupla
# lista:mantienen un orden y se pueden modificar, es mutable
# tupla:es inmutables
# set:no es completamente mutable ni inmutable,no mantienen ningun indice,no tiene
# un elemento tipo set

# tipo set
planetas = {'marte','jupiter','venus'}

# repaso de tuplas

tupla = (4, 'Hola', 6.78,[1,2,78], 4,'Hola')
print(tupla)

# podemos buscar un elemento

print(4 in tupla) # accion booleana,respuesta de tipo boole
# lo que usar dentro de las tuplas son: index,count,len

# se puede convertir de Tuplas a listas y de lista a tupla

