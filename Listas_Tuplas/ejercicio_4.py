#Escribir un programa que pregunte al usuario los números ganadores de la lotería, los almacene en una lista
# y los muestre por pantalla ordenados de menor a mayor.

list_contenedor = []

num_ganadores = input('Cuales son los números ganadores? ')
print(f"num_ganadores: {num_ganadores}")
formateado = num_ganadores.split(' ')

for index in formateado:
    list_contenedor.append(int(index))

list_contenedor.sort()
print(f"Números ordenados: {list_contenedor}")