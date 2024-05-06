import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from PyPDF2 import PdfMerger, PdfFileReader

# Preguntar al usuario por el tamaño de la hoja
print()
tamaño_hoja = input("¿Desea que el tamaño de la hoja sea A4 o A3?: ").upper()
print()
if tamaño_hoja != 'A4' and tamaño_hoja != 'A3':
    print("Opción no válida. Se utilizará A4 por defecto.")
    print()
    tamaño_hoja = 'A4'
    print()

if tamaño_hoja == 'A4':
    figsize = (210 / 25.4, 297 / 25.4)  # Tamaño A4 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 4
else:
    figsize = (420 / 25.4, 297 / 25.4)  # Tamaño A3 en orientación paisaje en milímetros (ancho, alto)
    x_position_max = 8

# Abre el archivo de Excel
datos = "prueba5_excel.xlsx"
df = pd.read_excel(datos, header=None)  # Leer datos de Excel

# Iterar sobre las filas del DataFrame
for idx, row in df.iterrows():
    # Filtrar valores NaN
    row = row.dropna()
    
    # print(f"Fila {idx+1}: {row}")     # Imprimir por consola filas excel para comprobar que se leen correctamente

    # Crear un nuevo grafo para cada fila
    G = nx.Graph()

    # Agregar nodos al grafo G
    for cell in row:
        G.add_node(cell)

    # Agregar conexiones entre nodos en la fila actual
    for i in range(len(row) - 1):
        G.add_edge(row[i], row[i+1])

    # Calcular posiciones de los nodos utilizando el algoritmo spring
    pos = nx.spring_layout(G)

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

    # Dibujar bordes
    nx.draw_networkx_edges(G, pos)

    # Dibujar etiquetas
    for node, (x, y) in pos.items():
        plt.text(x, y, node, ha='center', va='center')

    # Eliminar ejes
    plt.axis('off')

    # Guardar el gráfico como PDF
    plt.savefig(f'prueba6_diagrama_{idx+1}.pdf', format='pdf')

    # Cerrar la figura para liberar memoria
    plt.close()

    print(f"El diagrama de flujo para la fila {idx+1} se ha generado con éxito ")
    print()

# Crear un objeto para combinar PDFs
pdf_merger = PdfMerger()

# Nombre del archivo PDF combinado
pdf_combined_file = 'prueba6_diagrama_PDF_combinado.pdf'

# Agregar cada archivo PDF generado al objeto combinador de PDFs
for idx in range(len(df)):
    pdf_file = f'prueba6_diagrama_{idx+1}.pdf'
    pdf_merger.append(pdf_file)

# Guardar el archivo PDF combinado
with open(pdf_combined_file, 'wb') as output_pdf:
    pdf_merger.write(output_pdf)

print(f"Los diagramas de flujo se han combinado en el archivo: {pdf_combined_file}")
print()
