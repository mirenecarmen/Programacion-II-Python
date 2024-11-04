# importamos con * si queremos importar todas las clases juntas ¿?

from Persona2 import Persona2
print('creacion de objetos'.center(50,'-'))
persona5 = Persona2('Lionel','Messi',35)
persona5.mostrar_detalle()

if __name__ == '__main__':
    # 10.5 Comprobación del módulo principal en ejecución

    print(__name__)

# comprobancion del metodo principal

print('eliminacion de objetos'.center(50 ,'-'))

             #10.6 Destructor de objetos
# con el 'del' ahora eliminamos persona5

del persona5
