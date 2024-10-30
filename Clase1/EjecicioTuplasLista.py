'''
dada la siguiente tupla

 tupla = (13,1,8,3,2,5,8) # definimos la tupla
 crear una lista que solo incluya los numeros menores a 5
 e imprima por consola [1,3,2]

'''
tupla = (13,1,8,3,2,5,8) 
lista = [] # definimos los elementos de la lista

#filtramos los elementos a 5 de la tupla
for elemento in tupla:
    if elemento < 5:
        lista.append(elemento)
print(lista)
