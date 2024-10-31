# ejerci 9 : mostrar una frase sin espacion y contar su longitud
# hacer un programa donde el usuario ingrese una frase,se le devolverá
# la misma frase pero sin espacios en blanco,y ademas un contador de cuantos
# caracteres tiene la frase
# (sin contar los espacios en blanco)
# ej: frase : vivir por siempre en paz
# frase final = vivirporsiempreenpaz
# N° de caracteres = 20

frase1 = input("digite una frase:")
frase2 = " "
for i in frase1:
    if i != " ":
        frase2 + i
frase1 = frase2
print(f" frase final:{frase1} ")
print(f'numero de caracteres:{len(frase1)}')