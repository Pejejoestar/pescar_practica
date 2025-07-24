capital_a_invertir = int(input('Ingrese la cantidad a invertir: '))

tiempo_invertir = int(input('Ingrese la cantidad a años a invertir: '))
interes_anual = int(input('Ingrese el interés anual: '))

operacion = capital_a_invertir * (capital_a_invertir * (interes_anual / 100 + 1) ** tiempo_invertir)

print(f"El capital que recaudará será de: {operacion}")