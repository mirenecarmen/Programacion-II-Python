# import math ,clase math para hacer uso de la funcion sqrt(rainz cuadrada)
# sacar la raiz cuadrada de un numero positivo
import math

numero = int(input('digite un numero positivo'))
while numero < 0:
    print('Error : deberia se un numero positivo ')
    numero = int(input('digite un numero positivo: '))
print(f'la raiz cuadrada es: {math.sqrt(numero):.2f}')