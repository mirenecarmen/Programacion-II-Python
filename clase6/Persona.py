# creacion de objetos con argumentos

"""class Persona:# creamos la clase
    # creamos una plantilla que es la clase
    def __init__(self): # se lo llama metodo init dunder
        self.nombre = 'Juan'
        self.apellido = 'Zalar'
        self.edad = 22
persona1 = Persona() #constructor que apunta al init

# print(type(Persona))
print(persona1.nombre)
print(persona1.apellido)
print(persona1.edad)
# en python el constructor esta oculto
# llama a traves del self y del init a los objetos ¿?"""

# siguiente clase
class Persona:# creamos la clase
    # creamos una plantilla que es la clase
    def __init__(self,nombre,apellido,dni,edad,*args,kwargs): # se lo llama metodo init dunder
        self.nombre = nombre # atributos de metodos (no de clase)
        self.apellido = apellido
        self.edad = edad
        self._dni = dni # este atributo esta encapsulado
        #self.args = args
        #self.kwargs = kwargs

    def mostrar_detalle(self): # self es el equivalente a this en java
        print(f'Persona : {self.nombre} {self.apellido} {self.edad}')
persona1 = Persona('Ariel','Betancud',435243454,40) #constructor que apunta al init al que le estamos pasando argumentos
#tarea
print(f'el objeto1 de la clase persona es :{persona1.nombre} {persona1.apellido}.su edad es {persona1.edad}')


                              # Modificar atributos del objeto


# print(persona1.nombre)
# print(persona1.apellido)
# print(persona1.edad)

persona2 = Persona('Osv','Gioda',3223343,45)
print(f'el objeto2 de la clase persona es :{persona2.nombre} {persona2.apellido} .su edad es {persona2.edad}')

# referencia de persona objeto

persona1.nombre = 'Lil'
persona1.apellido = 'bucella'
persona1.edad = 40
print(f'el objeto1 modificado de la clase persona : {persona1.nombre} {persona1.apellido}.su edad es :{persona1.edad}')


                                  #8.7 Métodos de instancia. crear UML
# los atributos son caracteristicas
# los metodos son : el comportamiento que van a tener

# hay que respetra la tabulacion cuando creamos otro metodo def mostrar_detalle

# acceder a los atributos de un metodo,difencia entre self y def¿?
persona1.mostrar_detalle() # aqui la referencia se pasa de manera automatica,no se puede usar el self porque solo se usa en los metodo

persona2.mostrar_detalle()

# Persona.mostrar_detalle() --> esto ya no va,debemos pasarle una referencia para el self o dará error

           # 9.2 Crear atributos desde un objeto
# creamos un atributo pero no se comparte con los objetos ¿?
# persona1.telefono = '374261525'
persona1.telefono = '374261525'
print(f'este es el telefono de : {persona1.nombre} {persona1.telefono}')

# Sintesis,no se usa la creacion de un atributo desde un objeto ¿?

                                         # 9.7 Método init Dunder con argumentos variables


#encapsulamient

persona2.mostrar_detalle() #---> esta es la manera correcta de encapsular
# print(persona3._dni) --> esto no se debe (esta encapsulado)

# tambien se usa el doble guion bajo persona3.__nombre   << si lo ejecutamos no se ve porque esta encapsulado
