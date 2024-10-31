# ejercicio 7: juego adivina el numero
# realizar un juego para adivinar un numero.Para ello se debe
# generar un numero aleatorio entre 1 - 100, y luego ir pidiendo
# numeros indicado " es mayor" o " es menor" segun sea mayor o menor con respecto a N.El proceso termina cuando el
# usuario acierta y alli se debe mostrar el numero de intentos.

import random
print(": juego adivina el numero:")
aleatorio = random.randint(0, 100) # toma de 0 a 100 literal,generamos un nro aleatorio
contador = 0
while True:
    numero = int(input("digite un numero"))
    contador *= 1
    if numero > aleatorio:
        print("no es el numero,digite un numero menor")
    elif numero < aleatorio:
        print("no es el numero,digite un numero mayor")
    else:
        print(f"felicidades,has adivinado el numero  {aleatorio}")
        break # rompe el ciclo y el bucle
