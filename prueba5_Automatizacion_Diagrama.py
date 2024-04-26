# Cargar datos desde Excel
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx 
import openpyxl

# Open the Excel file
file_path = "prueba5_excel.xlsx"
workbook = openpyxl.load_workbook(file_path)

# Assuming you want to work with the first sheet, change this if needed
sheet = workbook.active

# Initialize an empty matrix
matrix = []

# Iterate through rows and columns and store values in the matrix
for row in sheet.iter_rows(values_only=True):
    row_values = []    
    for cell in row:
        row_values.append(cell)
        matrix.append(row_values)

# Close the workbook when done
workbook.close()

print(matrix)
""" 
# Crear un gráfico utilizando NetworkX
G = nx.Graph()

# Agregar nodos
for col in datos.columns:
    G.add_node(col)  # Añadir elemento como nodo

# Agregar conexiones entre elementos
for i in range(len(datos.columns) - 1):
    G.add_edge(datos.columns[i], datos.columns[i + 1])  # Añadir conexión entre elementos adyacentes

# Preguntar al usuario por el tamaño de la hoja
tamaño_hoja = input("¿Desea que el tamaño de la hoja sea A4 o A3?: ").upper()
if tamaño_hoja != 'A4' and tamaño_hoja != 'A3':
    print("Opción no válida. Se utilizará A4 por defecto.")
    tamaño_hoja = 'A4'

# Definir el tamaño del gráfico según la selección del usuario
pos = {}  # Inicializar el diccionario de posiciones
x_position = 0
y_position = 0 

if tamaño_hoja == 'A4':
    figsize = (210 / 25.4, 297 / 25.4)  # Tamaño A4 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 4
else:
    tamaño_hoja == 'A3'
    figsize = (420 / 25.4, 297 / 25.4)  # Tamaño A3 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 8

# Dibujar el gráfico con el tamaño adecuado
plt.figure(figsize=figsize)       

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

# Dibujar bordes
nx.draw_networkx_edges(G, pos)

# Dibujar etiquetas
for node, (x, y) in pos.items():
    plt.text(x, y, node, ha='center', va='center')

# Eliminar ejes
plt.axis('off')

# Guardar el gráfico como PDF
plt.savefig('prueba4_diagrama.pdf', format='pdf')

print("El diagrama de flujo se ha generado con éxito ") """