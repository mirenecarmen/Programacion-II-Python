# ejercicio 5: convertidor de temperaturas
# realizar dos funciones para convertir de grados celsius a farenheit
# y viceversa
# investigar las formulas

# funcion que convierte de celsius a farenheit

def celsius_farenheit(celsius):
    return celsius * 9 / 5 + 32 # la precedencia:multiplicacion,division,suma

# fucncion que convierte de farenheit a celsius
def farenheit_celsius(farenheit):
    return (farenheit - 32) * 5 / 9 # resptear la precedencia

celsius = float(input('digite el valor de celsius: '))
resultado = celsius_farenheit(celsius)
print(f'{celsius} C a F --> {resultado: .2f}')

farenheit = float(input('digite el valor de farenheit:'))
resultado = farenheit_celsius(farenheit) # reutilizamos la variable resultado
print(f'{farenheit} de F a C --> {resultado: .2f}')