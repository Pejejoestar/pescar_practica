#Leer un Excel  listar las columnas que contiene.
import pandas as pd

# Crear un DataFrame con 3 columnas y 15 filas vacías
data = {
    "Nombre": ["" for _ in range(15)],
    "Edad": ["" for _ in range(15)],
    "País": ["" for _ in range(15)]
}

df = pd.DataFrame(data)

# Guardar como archivo Excel
df.to_excel("datos_personales.xlsx", index=False)
