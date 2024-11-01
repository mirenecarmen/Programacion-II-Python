# funciones recursivas
# se manda a llamar a si misma para completar una cierta tarea
# la recursividad tiene 2 facetas:necesitamos un caso base y un caso recursivo (necesario para que no se haga infinita)

# funciones recursivas

def factorial(numero):
    if numero == 1: # caso base
        return 1
    else:
        return numero * factorial(numero -1) # caso recursivo
numeroFactorial = int(input('digite el numero para calcular el factorail:'))
# resultado = factorial(5) # lo hacemos en codigo duro
#print(f'el factorial del numero 5 es :{resultado}')

# tarea que el usuario ingrese el numero para calcular el factorial

print(f'el factorial del numero es :{numeroFactorial}')
