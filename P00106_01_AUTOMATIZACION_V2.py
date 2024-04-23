import pandas as pd

# Crear una matriz con letras y numeros
matriz = [
    ['a', 'b', 'c'],
    [1, 2, 3],
    [4, 5, 6]
]

# Convertir la matriz en un DataFrame de pandas
df = pd.DataFrame(matriz)

# Intercambiar filas y columnas
df = df.transpose()

# Establecer nombres de columna (letras)
df.columns = ['A', 'B', 'C']

# Establecer nombres de fila (números)
df.index = [1, 2, 3]

# Establecer nombres combinaciones
for columna in df.columns:
    for fila in df.index:
        nombre_celda = columna + str(fila)
        df.loc[fila, columna] = nombre_celda

print(df)


