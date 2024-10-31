# ejercicio 5 : factorial de un numero positivo

# hacer un programa para calcular el factorial de un numero positivo

numero = int(input("digite un numero:"))
while numero < 0: # mientras el nro sea negativo
    print("error -> el nro tiene que ser positivo")
    numero = int(input("digite un numero:"))
factorial = 1 # la variable para calcular el factoria
for i in range( 1, numero+1):
    factorial *= i
print(f" el factrial del numero {numero} positivo ingresado es : {factorial}")
