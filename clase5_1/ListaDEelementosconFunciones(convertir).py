# distintos tipos de datos como argumentos
# lo que haremos es definir una funciona que reciba una lista y reciba unos elementos
# se convierte a tupla o lista segun
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)
nombres2 = ['tito','Pedro','Carlos']
desplegarNombres(nombres2)
desplegarNombres('Carla')

# desplegarNombres(10,11) no es un objeto iterable

desplegarNombres((10,11)) # ya se convierte en una tupla,es decir para correun un nro tuvimos que convertira  a tupla
#desplegarNombres((10,))  debe quedar si o si el elemento con la coma para que se convierta en tupla
desplegarNombres([22,55]) # convertimos en lista