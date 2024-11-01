def sumar(a = 0, b= 0):
    return a + b
resultado = sumar()
print(f'resultado de la suma:{resultado}')

# si le damos un valor por default podemos hacer lo siguiente
def sumar2(a = 0, b= 0):
    return a + b
resultado = sumar2()
print(f'resultado de la suma:{resultado}')
print(f'resultado de la suma:{sumar2(22,66)}')