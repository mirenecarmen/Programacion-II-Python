#Colas con Listas Cola = QUEue
# Estructuras de datos de tipo fifo (first input /first output)

cola = ["Ana", "Luis", "Carlos", "Marta"]

# agregamos elementos al FINAL de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# sacamos elementos de la cola
seRetira= cola.pop(0)
print(f'Atendido el cliente : {seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente : {seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente : {seRetira}')
print(cola)

seRetira= cola.pop(0)
print(f'Atendido el cliente : {seRetira}')
print(cola)