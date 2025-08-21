#Cargar un archivo CSV y mostrar sus primeras 10 filas.

import csv
#import pandas as pd

with open ('./datos.csv', newline="", encoding="utf-8") as f:
    data = csv.reader(f)
    index = 0
    for fila in data:
        index += 1
        print(fila)

        if index == 11:
            break


#df = pd.read_csv('datos.csv')
