class Persona2:              # creamos la clase
    # creamos una plantilla que es la clase
    def __init__(self,nombre,apellido,edad): # se lo llama metodo init dunder
        self._nombre = nombre # atributos de metodos (no de clase)
        self._apellido = apellido # ponemos el guin bajo,lo encapsulamso
        self._edad = edad

    def mostrar_detalle(self): # self es el equivalente a this en java
        print(f'los datos a mostrar son los siguientes: {self._nombre}{self._apellido}{self._edad}')
# insertamos un decorador con el @ y el metodo getter
    @property #decorador
    def nombre(self): # mrtodo geter
        print('estamos usando el metodo get')
        return self._nombre

    @nombre.setter
    def nombre(self,nombre): # metodo setter
        print('estamos usando el metodo set')
        self._nombre = nombre

# tarea: agrear get y set para los otros dos atributps

    @property #decorador
    def apellido(self): # mrtodo geter
        return self._apellido

    @apellido.setter
    def apellido(self,apellido): # metodo setter
        self._apellido = apellido


    @property #decorador
    def edad(self): # mrtodo geter
        return self._edad

    @edad.setter
    def edad(self,edad): # metodo setter
        self._edad = edad

    def __del__(self):
        print(f'Persona2:{self._nombre} {self._apellido} {self._edad}')

if __name__ == '__main__':
    persona1 = Persona2('Ariel','Betancud',41)

    print(persona1.nombre) # llamamos al metodo getter
    #persona1.nombre = 'juan pedro' # llamamos al metodo setter
    print(persona1.apellido) # otra vez con el metodo getter
    print(persona1.edad)
    print(persona1.mostrar_detalle()) # llamamos al metodo mostrar_detalles

     # 10.2 Atributos read-only (solo lectura)
     # comentamos el setter de edad

     #persona1.edad=40
     #print(persona1.edad)
    #
    # dará error,nos demuestra que si eliminamos el setter
     # se transformaria el atrubuto en un read only,porque no tiene el metodo set para ser modificada
     # porque al no tener el setter significa que edad esta ENCAPSULADA,PODEMOS IMPRIMIR PERO NO MODIFICAR

    # EL ATRUBUTO QUE NO TIENE SET SE LLAMA READ ONLY O SEA SOLO LECTURA

    #10.3 Tarea: Con la clase Persona2: ver el principio del video para aclarar dudas sobre la tarea
    '''
    DEMOSTRAR   que con el encapsulamiento no se puede acceder a los atributos fuera
    de la clase
    '''
    persona1.edad=40
    print(persona1.edad)

    '''
    el met geter usamos el property
    en el seter necesitamos el self,y necesita que le pasemos un parametro
    '''

    # tarea:crear tre objetos mas,instanciarlos,usando los metodos getter and setter
    # para modificar y mostrar los cambios ,luego los mostramos desde mostrar_detalles

    # objeto 1 de la tarea
    persona2 = Persona2('flor','romero',23)
    persona2.nombre = 'florencia'
    persona2.apellido = 'romero'
    persona2.edad = 23
    print(persona2.nombre)
    print(persona2.apellido)
    print(persona2.edad)
    persona2.mostrar_detalle()

    # objeto 2 de la taarea
    persona3 = Persona2('firu','mach',23)
    persona3.nombre = 'firu'
    persona3.apellido = 'mach'
    persona3.edad = 23
    print(persona3.nombre)
    print(persona3.apellido)
    print(persona3.edad)
    persona3.mostrar_detalle()

    # objeto 3 de la tarea
    persona4 = Persona2('coco','me',23)
    persona4.nombre = 'coco'
    persona4.apellido = 'me'
    persona4.edad = 23
    print(persona4.nombre)
    print(persona4.apellido)
    print(persona4.edad)
    persona4.mostrar_detalle()

    print(__name__) # nos dice donde se esta ejecutando ,aparecerá en Persona2 y en pruebapersona

    #