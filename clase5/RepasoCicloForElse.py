numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
else:
    print('esto se termina')

# aun con la lista vacia se ejecuta el else
numbers = []
for n in numbers:
    print(n)
else:
    print('esto se termina')

# la unica manera para que no se ejecute el else es usando
# un condicional y poniendo un break

numbers = [1,2,3,4,5]
for n in numbers:
    print(n)
    if n == 3:
        break
else:
    print('esto se termina')