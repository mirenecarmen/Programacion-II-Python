def show(name, lastName):
    print(name+' '+lastName)
person = ['Ariel','Betancud']
show(person[0],person[1]) # pasamos uno por uno los datos de la lista a la funcion
show(*person) # esto es lo mismo que lo anterio pero le pasamos tooo junto


#ests es la forma de desmpaquetar una funcion

person2 = ('osvaldo','giord') # desemapquetmos a traves de una tupla
show(*person2)
#ahora desempaquetamos a traves de diccionarios
person3 = {'lastName':'lucero','name':'natalia'}
show(**person3)