# escriba un programa donde cree una lista con los sigueintes personasjes
# del señor de los anillos

# nombre : Aragon
# clase : guerrero
# raza : dunadan del norte

# nombre : Gandalf
# clase : mago
# raza : istar

# nombre : Legolas
# clase : arquero
# raza : elfo sindar

personajes = [] # creamos una lista vacia
#creamos diccionarios (tienen {})

P = {
    "nombre": "Aragon",
    "clase": "guerrero",
    "raza": "dunadan del norte"
}
personajes.append(P) # agregamos a la lista un personaje

P = {
    "nombre": "Gandalf",
    "clase": "mago",
    "raza": "istar"
}
personajes.append(P) # agregamos a la lista un personaje
P = {
    "nombre": "Legolas",
    "clase": "arquero",
    "raza": "elfo sindar"
}
personajes.append(P) # agregamos a la lista un personaje
print(personajes)

#agregar por lo menos otros 3 personajes
