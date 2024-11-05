class Vehiculo:
    '''
    definir una clase padre llamada vehiculo y dos clases hijas llamadas
    auto y bicicleta,las cuales hererdan de la clase padre vehiculo.
    La clase padre debe tener los siguientes atributos y metodos:
    vehiculo (clase padre)
    -atributos (color ,ruedas)
    .metodos (__init__(color,ruedas) y __str__()

    auto (clase hija de vehiculo
    -atributos (velocidad km/h
    -metodos __init__(color,ruedas,velocidad) y __str__()

    bicicleta(clase hija de vehiculo)
    -atributos (tipo (urbana,montaña etc)
    -metodos __init__(color,ruedas,tipo) y __str__()

    crear un objeto de cada clase

    '''

    def __init__(self, color, ruedas):
        self._color = color
        self._ruedas = ruedas

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def ruedas(self):
        return self._ruedas

    @ruedas.setter
    def ruedas(self, ruedas):
        self._ruedas = ruedas

    def __str__(self):
        return f"Vehiculo(Color: {self._color}, Ruedas: {self._ruedas})"


class Auto(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self._velocidad = velocidad

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    def __str__(self):
        return f"Auto(Color: {self._color}, Ruedas: {self._ruedas}, Velocidad: {self._velocidad} km/h)"


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self._tipo = tipo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, tipo):
        self._tipo = tipo

    def __str__(self):
        return f"Bicicleta(Color: {self._color}, Ruedas: {self._ruedas}, Tipo: {self._tipo})"


# Crear un objeto de cada clase
vehiculo1 = Vehiculo('Rojo', 4)
auto1 = Auto('Azul', 4, 120)
bicicleta1 = Bicicleta('Verde', 2, 'Montaña')

# Mostrar los objetos creados
print(vehiculo1)
print(auto1)
print(bicicleta1)