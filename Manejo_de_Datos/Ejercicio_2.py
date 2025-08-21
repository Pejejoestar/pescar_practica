#Leer un JSON y acceder al valor de una clave específica
import json
with open ('./data.json', "r", encoding="utf-8") as f:
    data = json.load(f)
    print(data[1])
    print(data[1]['Hermanos'][1])
