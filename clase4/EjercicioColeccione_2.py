# ejercicio 2: operaciones de conjuntos con listas

# escriba un programa que tenga 2 listas y que a continuacion
#cree las siguientes lista (en las que no deben haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Listas de palabras que aparecen en la primera lista,pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista,pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

Lista1 = [1, 2, 4, 5, 6, 7, 6, 9, 10, 11, 12]
Lista2 = [4, 14, 15, 4, 17, 18, 19, 20, 21, 22, 23]

#Eliminar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(Lista1)
conjunto2 = set(Lista2)

union = list(conjunto1 | conjunto2) # unimos los dos conjuntos
solo1= list(conjunto1 - conjunto2) # solo muestra el conjunto 1
solo2 = list(conjunto2 - conjunto1) # solo muestra el cnjutno2
interseccion = list(conjunto1 & conjunto2) # mostramos amabas listas

print(f'Lista de palabras que aparecen en las listas: {union}')
print(f'Listas de palabras que aparecen en la primera lista,pero no en la segunda{solo1}')
print(f'Lista de palabras que aparecen en la segunda lista,pero no en la primera:{solo2}')
print(f'Lista de palabras que aparecen en ambas listas:{interseccion}')