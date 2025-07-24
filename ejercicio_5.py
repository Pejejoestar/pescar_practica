horas_llevadas = int(input('¿Cuantas horas trabajaste hoy? '))
precio_por_hora = 100

if horas_llevadas < 0:
    print("Debe de ingresar un número mayor a 0")
else:

    sueldo_total = horas_llevadas * precio_por_hora

    print(f'Tu sueldo es de {sueldo_total}')