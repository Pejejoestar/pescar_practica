
def ConsultaNumero():
    num_usuario = int(input('Ingrese un número '))
    return num_usuario

valor_usuario = ConsultaNumero()

def Validacion(num_usuario: int):
    contenedor_suma = 0

    valor_recibido = num_usuario
    
    if valor_recibido < 0:
        print("ERROR: Ingrese un número mayor a 0")
        nuevo_vaor = ConsultaNumero()
        Validacion(nuevo_vaor)
    else:
        print(f"valor_recibido: {valor_recibido}")
        for index in range(valor_recibido):
            valor_indice = index + 1
            contenedor_suma = contenedor_suma + valor_indice
    print(f'Suma total: {contenedor_suma}')

Validacion(valor_usuario)