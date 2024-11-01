# definimos la funcion pero no sabemos cuantos van a ser
def listaNombres(*nombres):
    for nombre in nombres: # el argymento se convierte en tupla
        print(nombre)
listaNombres('Luscas','jose','claudia','rosa','-maria')
# que psaria si le aumento argumentos/elementos?se seguiran aumentando
# cada vez que llama a la funcion recibe mas arguments
listaNombres('marcos','malvina','helecho','pino','oro')
# normalmente la sintaxis es *args