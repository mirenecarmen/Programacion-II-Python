class Persona:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad

    # Decorador @property para el atributo nombre
    @property
    def nombre(self):
        return self._nombre

    # Decorador setter para el atributo nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    # Decorador @property para el atributo edad
    @property
    def edad(self):
        return self._edad

    # Decorador setter para el atributo edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): # override o sobreescribir
        return f'Persona: [ nombre: {self._nombre},edad: {self._edad}]'


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    # Decorador @property para el atributo sueldo
    @property
    def sueldo(self):
        return self._sueldo

    # Decorador setter para el atributo sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self): # override o sobreescribir
        return f'Empleado: [ Sueldo : {self._sueldo}]{super().__str__()} ]'




# Crear un objeto de la clase Empleado
empleado1 = Empleado('Ariel', 40, 7500)

# Mostrar los datos usando los getters
print("Datos del empleado:")
print("Nombre:", empleado1.nombre)   # Ahora se puede acceder directamente sin get_nombre()
print("Edad:", empleado1.edad)
print("Sueldo:", empleado1.sueldo)

# Modificar los datos usando los setters
empleado1.nombre = 'Carlos'
empleado1.edad = 45
empleado1.sueldo = 8000

# Mostrar los datos nuevamente después de la modificación
print("\nDatos del empleado modificados:")
print("Nombre:", empleado1.nombre)
print("Edad:", empleado1.edad)
print("Sueldo:", empleado1.sueldo)

