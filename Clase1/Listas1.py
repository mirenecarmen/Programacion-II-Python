# Lista = Ariel,Liliana,Natalia,Osvaldo
# las listas es lo que se conoce en otros lenguajes
# como ARRAYS o ARREGLOS o VECTORES
# UNA LISTA PUEDE TENER DIFERENTES TIPOS DE DATOS
nombres = [ "naty","osvaldo","lily","ariel"]
print(nombres)

#print(nombres[0])
#print(nombres[1])
#print(nombres[3])

#print(nombres[-1])
#print(nombres[-2])

print(nombres[0:2]) # solo muestra el indice 0,1 pero no el indice 2
# ir al inicio de la lista al indice (sin incluirlo)

print(nombres[ :3]) # indices a mostrar 0,1,2
#desde el inidce indicado hasta el final
print(nombres[0:2]) # solo muestra el indice 0,1 pero no el indice 2
# ir al inicio de la lista al indice (sin incluirlo)

print(nombres[1: ])

#modificamos un valor
nombres[2] = "Liliana"

nombres[0] = "Natalia"
print(nombres)
# iterar una lista
for nombre in nombres: # nombre es singular,la lista es plural
    print(nombre)
else:
    print("se acabaron los elementos de la lista")

# preguntamos cuantos elementos tiene
print(len(nombres)) # le pasamos como parametro la lista

# agregamos un elemento
nombres.append("marcelo")
nombres.append([1, 2, 3])
nombres.append(True)
nombres.append(10.05)
nombres.append([4 , 5])
nombres.append(7)
print(nombres)

# insertar un elemento en un indice especifico

nombres.insert(1,"alberto")
print(nombres)
nombres.insert(3,"debora")
print(nombres)

# eliminamos un elementos

nombres.remove("alberto")
print(nombres)

#elimienar el ultimo elemento
nombres.pop()
print(nombres)

# eliminar un indice especidifo

del nombres[2] # del significa eliminar
print(nombres)

# eliminar,borrar o limpiar todos los elementos

nombres.clear()
print(nombres)

# eliminar la lista
del nombres
print(nombres)

# concatenar elementos

Lista1 = [1, 2, 3, 1]
Lista2 = [4, 5, 6, 1]
Lista3 = Lista1+Lista2
print(Lista3)

Lista3.extend([7, 8, 9]) # funcion para agregar varios elementos a una lista
print(Lista3)

print(Lista3.index(5)) # funciona para ubicar en que indice sta el valor ingresado


# como saber cuantos valores repetidos hay dentro de una lista
print(Lista3.count(1))

# para poner la lista al reves
Lista3.reverse()
print(Lista3)

# para que una lista se multiplique repitiendo sus elementos
Lista3 = Lista3 * 2
print(Lista3)

#Metodos de ordenamiento

Lista3.sort() # ordena los elementos de forma ascendente
print(Lista3)

Lista3.sort(reverse=True) # de forma descendente
print(Lista3)



