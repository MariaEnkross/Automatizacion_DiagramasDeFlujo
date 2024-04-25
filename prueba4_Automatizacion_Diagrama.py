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
pos = {}  # posición
x_position = 0
y_position = 0
for node in G.nodes():
    if x_position == 1 or x_position == 3:  # Si es el primer nodo o el tercer nodo, dibujamos un rombo
        pos[node] = (x_position, y_position)  # Posición para el primer nodo
        nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=3000, node_shape='d', node_color='skyblue', label=node)
    else:
        if x_position < len(G.nodes()) - 2:  # Si es un nodo distinto al primero o al tercero, dibujamos un rectángulo
            pos[node] = (x_position, y_position)  # Posición para todos los nodos excepto los dos últimos
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=3000, node_shape='s', node_color='lightgreen', label=node)
        else:  # Si es uno de los dos últimos nodos, movidos hacia la izquierda y hacia abajo
            pos[node] = (x_position - 4, - 3)
            y_position = 0.5
            nx.draw_networkx_nodes(G, pos, nodelist=[node], node_size=3000, node_shape='s', node_color='lightgreen', label=node)
    x_position += 1

# Dibujar bordes
nx.draw_networkx_edges(G, pos)

# Dibujar etiquetas
for node, (x, y) in pos.items():
    plt.text(x, y, node, ha='center', va='center')

# Eliminar ejes
plt.axis('off')

# Guardar el gráfico como PDF
plt.savefig('prueba4_diagrama.pdf', format='pdf')

# Mostrar el gráfico en pantalla
plt.show()

print("El diagrama de flujo se ha generado con éxito ")
