import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx 
import openpyxl

# Preguntar al usuario por el tamaño de la hoja
tamaño_hoja = input("¿Desea que el tamaño de la hoja sea A4 o A3?: ").upper()
if tamaño_hoja != 'A4' and tamaño_hoja != 'A3':
    print("Opción no válida. Se utilizará A4 por defecto.")
    tamaño_hoja = 'A4'
    print()

if tamaño_hoja == 'A4':
    figsize = (210 / 25.4, 297 / 25.4)  # Tamaño A4 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 4
else:
    tamaño_hoja == 'A3'
    figsize = (420 / 25.4, 297 / 25.4)  # Tamaño A3 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 8

# Abre el archivo de Excel
datos = "prueba5_excel.xlsx"
workbook = openpyxl.load_workbook(datos)
sheet = workbook.active

# Crear un gráfico utilizando NetworkX
G = nx.Graph()

# Inicializa una lista vacía para contener las filas/columnas no vacías
rows = []
cols = []

""" # Itera a través de todas las filas y guarda
for row in sheet.iter_rows(values_only=True):
    if any(cell is not None for cell in row):
        rows.append(row)

# Itera a través de todas las columnas y guarda
for col in sheet.iter_cols(values_only=True):
    if any(cell is not None for cell in col):
        cols.append(col)

# Iterar sobre las filas no vacías
for row_data in rows:
    # Agregar nodos al grafo G
    for node in row_data:
        if node is not None:
            G.add_node(node) 

# Iterar sobre las columnas no vacías
for col_data in cols:
    # Agregar conexiones entre nodos al grafo G
    for i in range(len(col_data)):
        for j in range(i+1, len(col_data)):
            if col_data[i] is not None and col_data[j] is not None:
                G.add_edge(col_data[i], col_data[j]) 
 """
# Dibujar el gráfico con el tamaño adecuado
plt.figure(figsize=figsize)   

pos = {}  # Inicializar el diccionario de posiciones
x_position = 0
y_position = 0 

for node in G.nodes():
    pos[node] = (x_position, y_position)
    if x_position == 0 or x_position % 2 == 0:
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=3000, node_shape='s', node_color='skyblue')
    else:
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=3000, node_shape='d', node_color='lightgreen')

    if x_position < x_position_max:
        x_position += 1

    else:
        x_position = 1
        y_position -= 1

    if y_position < -6:
        y_position = x_position - 1

    if y_position is None:
        x_position = 0
        y_position = x_position - 1
        break

# Dibujar bordes
nx.draw_networkx_edges(G, pos)

# Dibujar etiquetas
for node, (x, y) in pos.items():
    plt.text(x, y, node, ha='center', va='center')

# Eliminar ejes
plt.axis('off')

# Guardar el gráfico como PDF
plt.savefig('prueba5_diagrama.pdf', format='pdf')

# print("El diagrama de flujo se ha generado con éxito ")
print() 