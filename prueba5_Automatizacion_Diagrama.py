import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx 
import openpyxl

# Preguntar al usuario por el tamaño de la hoja
tamaño_hoja = input("¿Desea que el tamaño de la hoja sea A4 o A3?: ").upper()
if tamaño_hoja != 'A4' and tamaño_hoja != 'A3':
    print("Opción no válida. Se utilizará A4 por defecto.")
    tamaño_hoja = 'A4'

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

# Inicializa una lista vacía para contener las filas/columnas no vacías
rows = []
cols = []

# Itera a través de las filas y guarda las que no están vacías en la lista
for row in sheet.iter_rows(values_only=True):
    if any(cell is not None for cell in row):
        rows.append(row)

# Crear un gráfico utilizando NetworkX
G = nx.Graph()

# Recorrer las filas
for row in rows:
    G.add_node(row)  # Agregar el nodo correspondiente a la fila

   # Inicializar el índice
    i = 0

    # Recorrer los elementos de la fila
    while rows[row][i] is not None:
        G.add_node = rows[row][i]
        i+=1

"""
for row in rows:
    G + string[row] = nx.Graph()
    i=0

    while rows[row][i] != None:
        G.add_node = rows[row][i]
        i+=1
    
    G.string[row] = G

# Agregar nodos
for row in rows:
    while cell in row:
        if cell is not None:
            G.add_node(cell)  # Añadir elemento como nodo

# Agregar conexiones entre elementos
for i in range(len(rows) - 1):
    for j in range(len(rows[i])):
        # Verificar si las celdas no son None antes de agregar la conexión
        if rows[i][j] is not None and rows[i + 1][j] is not None:
            G.add_edge(rows[i][j], rows[i + 1][j])  # Añadir conexión entre elementos adyacentes
  
# Preguntar al usuario por el tamaño de la hoja
tamaño_hoja = input("¿Desea que el tamaño de la hoja sea A4 o A3?: ").upper()
if tamaño_hoja != 'A4' and tamaño_hoja != 'A3':
    print("Opción no válida. Se utilizará A4 por defecto.")
    print()
    tamaño_hoja = 'A4'

# Definir el tamaño del gráfico según la selección del usuario
pos = {}  # Inicializar el diccionario de posiciones
x_position = 0
y_position = 0 

if tamaño_hoja == 'A4':
    figsize = (210 / 25.4, 297 / 25.4)  # Tamaño A4 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 4
else:
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
plt.savefig('prueba4_diagrama.pdf', format='pdf')

print("El diagrama de flujo se ha generado con éxito ")
print()

 """