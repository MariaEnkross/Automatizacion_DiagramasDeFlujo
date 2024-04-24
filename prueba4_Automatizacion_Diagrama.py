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
plt.figure(figsize=(297 / 25.4, 210 / 25.4))  # Tamaño A4 en orientación paisaje en milímetros (ancho, alto)
pos = {}                                      # posición
x_position = 0
for node in G.nodes():
    if x_position < len(G.nodes()) - 2:
        pos[node] = (x_position, 0)  # Posición para todos los nodos excepto los dos últimos
    else:
        pos[node] = (x_position - 4, -3)  # Posición para los dos últimos nodos, movidos hacia la izquierda y hacia abajo
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
