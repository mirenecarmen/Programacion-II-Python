# ejercicio 11: agenda telefonica
# hacer un programa que simule una agenda de contactos.Crear un diccionario
# donde la clase sea el nombre del usuario y el valor sea el telefono,el programa
# tendra el siguiente menu de opciones:
# 1. Nuevo Contacto
# 2. Borrar contacto
# 3. Ver contactos existentes
# 4. Salir

agenda = {}

while True:
    print('Menu:')
    print("1. Nuevo Contacto")
    print("2. Borrar contacto")
    print("3. Ver contactos existentes")
    print("4. Salir")

    opcion = int(input(" digite una opcion de menu:"))
    if opcion ==1 :
        nombre = input("digite el nombre del contacto:")
        telefono = input("digite el numero de telefono:")

        if nombre not in agenda:
            agenda[nombre] = telefono
            print("contacto agreado exitosamente.")

        else:
            print("este numero de contacto ya existe")
    elif opcion == 2:
        nombre = input("Cual es el nombre del contacto?")
        telefono = input("digite el numero de telefono:")

        if nombre in agenda:
            del (agenda[nombre])
            print("se ha eliminado el contacto")

        else:
            print("este contacto no existe en la agenda")

    elif opcion == 3:
        print ("agenda de contactos")
        for clave, valor in agenda.items():
            print(f'nombre: {clave},telefono: {valor}')

    elif opcion == 4:
        print('gracias por usar su agenda de contaxtos')
        break
    else:
        print('se equivoco de menu')
    print()







