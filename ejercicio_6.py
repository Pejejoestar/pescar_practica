num_usuario = int(input('Ingrese un número '))
contenedor_suma = 0
for index in range(num_usuario):
    valor_indice = index + 1
    contenedor_suma = contenedor_suma + valor_indice

print(f'Suma total: {contenedor_suma}')
