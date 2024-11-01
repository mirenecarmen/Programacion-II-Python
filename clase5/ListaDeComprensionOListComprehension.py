# list comprehension
# sirve para tomar lo necesario de una lista,no hacer ningun tipo de modificacion
# sobre ella (se puede usar en listas,tuplas,diccionario..)
#

names = ["Alice", "Bob", "Charlie", "Diana"]
alongP = [p for p in names if p[0] == 'p'] # esto regresa una nueva lista
print(alongP)

bottleC = [
    {"name": "Heineken", "country": "Netherlands"},
    {"name": "Corona", "country": "Mexico"},
    {"name": "Budweiser", "country": "USA"},
    {"name": "Guinness", "country": "Ireland"},
    {"name": "Quilmes", "country": "Arg"}
]

Arg = [ b for b in bottleC if b['country'] == 'Arg']
print(Arg)
print(bottleC)
# se creaa otro diccionario donde alli se extrae lo que necesitamos