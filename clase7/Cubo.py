class Cubo:
    '''
    crear la clase Cubo con los atributos ,ancho,alto y profundidad,con
    un metodo calcular_volumen que tendrá la formula:
    volumen = ancho * altura * profundidad
    que el usuario ingrese los valores
    '''

    def __init__(self,ancho,altura,profundidad):
        self.ancho = ancho
        self.altura = altura
        self.profundidad = profundidad

    def calcular_volumen(self):
        return self.ancho*self.altura*self.profundidad

ancho = int(input('digite el ancho del cubo:'))
altura = int(input('digite el altura del cubo:'))
profundidad = int(input('digite la profundidad del cubo:'))

cubo1 = Cubo(ancho, altura, profundidad)
print(f'el volumen del cubo es :{cubo1.calcular_volumen()}')