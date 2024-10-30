#pilas usando listas
pila = [1,2,3]

# agregar elementos a la pila al final
pila.append(4)
pila.append(5)
print(pila)

# sacamos elementos desde el final
elementoBorrado = pila.pop() # quita el ultimo elemento y lo guarda en la variable
print(f'sacamos el elemento: {elementoBorrado}')
print(f'la pila ahora quedo asi:{pila}')
