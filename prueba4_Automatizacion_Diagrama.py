import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Cargar datos desde Excel
datos = pd.read_excel('diagrama1.xlsx', header=None)  # No usar la primera fila como encabezados

# Crear un gráfico utilizando NetworkX
G = nx.Graph()

# Agregar nodos
for col in datos.columns:
    G.add_node(datos[col].iloc[0])  # Añadir elemento como nodo

# Agregar conexiones entre elementos
for i in range(len(datos.columns) - 1):
    G.add_edge(datos[i].iloc[0], datos[i + 1].iloc[0])  # Añadir conexión entre elementos adyacentes

# Dibujar el gráfico
plt.figure(figsize=(10, 6)) # tamaño
pos = {}                    # posicion
x_position = 0
for node in G.nodes():
    pos[node] = (x_position, 0)
    x_position += 1

# Dibujar bordes
nx.draw_networkx_edges(G, pos)

# Dibujar etiquetas
for node, (x, y) in pos.items():
    plt.text(x, y, node, ha='center', va='center', bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

# Eliminar ejes
plt.axis('off')

# Guardar el gráfico como PDF
plt.savefig('prueba4_diagrama.pdf', format='pdf')

# Mostrar el gráfico en pantalla
plt.show()

print("El diagrama de flujo se ha generado con éxito ")