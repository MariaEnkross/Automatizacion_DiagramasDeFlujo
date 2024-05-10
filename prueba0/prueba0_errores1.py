import pandas as pd

# Crear una matriz con letras y numeros
matriz = []

# Convertir la matriz en un DataFrame de pandas
df = pd.DataFrame(matriz)

# Intercambiar filas y columnas
df = df.transpose()

# Establecer nombres de columna (letras)
df.columns = ['A', 'B', 'C']

# Establecer nombres de fila (números)
df.index = [1, 2, 3]

# Establecer nombres combinaciones
# for columna in df.columns:
#     for fila in df.index:
#         nombre_celda = columna + str(fila)
#         df.at[fila, columna] = nombre_celda


print(df) #print del df completo
print(df.at[1,'A']) #print del df con coordenadas con nombre
print(df.iat[0,0]) #print del df con coordenadas tipo matriz

print(matriz)
print(matriz[0] [0])




