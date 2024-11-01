# kwargs key word arguments
# un tipo es para diccionario y otro para tuplas de terminos variables

def listarTerminos(**terminos): # lo mas usado es **kwargs para recibir los argumentos
    for llave, valor in terminos.items():
        print(f'{llave}:{valor}')

listarTerminos() # no recibe nada,nada se va a mostrar
listarTerminos(IDE = 'integrated development environment',PK= 'primary key')
listarTerminos(nombre='leonel messi')