#Ejercicio 1: eliminar duplicados de una lista
# escriba un programa donde tenga una lista y que a continuacion
# elimine los elementos repetidos,por ultimo mostrar la lista

# creamos la lista
lista = [ 1,2,3,'Ariel',7,7,3,'Alberto',1,'Ariel',2,'Alberto']
conjunto = set(lista) # convertimos la lista a un conjunto de tipo set
# lista = list(conjunto) # convertimos el conjunto a una lista
lista = list(set(lista)) # la conversion hecha en una sola linea de codigo (eficiente)
print(lista)