Selecciones = {
    10 : {
        "nombre": "Lionel Messi",
        "edad": 36,
        "altura": 1.70,
        "precio": 50000000,  # en euros
        "posición": "Delantero"
    },
    11 : {
        "nombre": "Cristiano Ronaldo",
        "edad": 39,
        "altura": 1.87,
        "precio": 30000000,  # en euros
        "posición": "Delantero"
    },
    24 : {
        "nombre": "Kylian Mbappé",
        "edad": 25,
        "altura": 1.78,
        "precio": 180000000,  # en euros
        "posición": "Delantero"
    },
    19 : {
        "nombre": "Kevin De Bruyne",
        "edad": 32,
        "altura": 1.81,
        "precio": 85000000,  # en euros
        "posición": "Centrocampista"
    },
    1 : {
        "nombre": "Virgil van Dijk",
        "edad": 32,
        "altura": 1.93,
        "precio": 70000000,  # en euros
        "posición": "Defensa"
    },
    4 : {
        "nombre": "Alisson Becker",
        "edad": 31,
        "altura": 1.91,
        "precio": 60000000,  # en euros
        "posición": "Portero"
    },
    7 : {
        "nombre": "Robert Lewandowski",
        "edad": 35,
        "altura": 1.85,
        "precio": 45000000,  # en euros
        "posición": "Delantero"
    },
    8 : {
        "nombre": "Luka Modrić",
        "edad": 38,
        "altura": 1.72,
        "precio": 10000000,  # en euros
        "posición": "Centrocampista"
    },
    5 : {
        "nombre": "Sergio Ramos",
        "edad": 37,
        "altura": 1.84,
        "precio": 8000000,  # en euros
        "posición": "Defensa"
    },
    3 : {
        "nombre": "Manuel Neuer",
        "edad": 38,
        "altura": 1.93,
        "precio": 12000000,  # en euros
        "posición": "Portero"
    }
}
# mostrando como recorrer un diccionario con el ciclo for
for i in Selecciones:
    print(f'{i} -> {Selecciones[i]}')