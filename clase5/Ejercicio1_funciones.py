# ejercicio 01: crear una funcion para sumar los valores recibidos de tipo
# numericos,utilizando argumentos ,variables *args como parametro de la
# funcion y agregar como resultado la suma de todos los valores pasados
# como argumentos

# definimos la funcion

def sumar_valor(*args): # recibimos una cantidad de parametros indefinidos
   # pass
   
    resultado = 0
   
   # iteramos cada eleemnto
    for valor in args:
       resultado += valor
    return resultado

# llamamos a la funcion
print(sumar_valor(3,5,9))