class Aritmetica:

    '''
el nombre de este tipo de comentario es: DocString
esto es documentacion de la clase de python
vamos a hacer en esta clase algunas operaciones de : suma ,resta,multip y d
    '''

    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    # metodo para sumar
    def sumar(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(7,9) # le pasamos los argumentos para los operandos
print(aritmetica1.sumar())

print(f'la resta de los numeros es: {aritmetica1.resta()}')
print(f'la mult de los numeros es: {aritmetica1.multiplicar()}')
print(f'la div de los numeros es: {aritmetica1.dividir():.2f}')

#9.4 Clase Aritmética: Resta, multiplicación y división

