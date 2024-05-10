import matplotlib
matplotlib.use('pdf')  # Configura el backend de Matplotlib en PDF
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import networkx as nx
import xlwings as xw
from PyPDF2 import PdfMerger
from io import BytesIO

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
    figsize = (420 / 25.4, 297 / 25.4)  # Tamaño A3 en milímetros (ancho, alto)
    x_position_max = 8

# Crear un objeto para combinar PDFs
pdf_merger = PdfMerger()

# Abrir el archivo de Excel con xlwings
app = xw.App(visible=False)
wb = app.books.open('prueba9_excel.xlsm')
sheet = wb.sheets[0]

# Leer datos desde Excel
df = sheet.used_range.value

# Iterar sobre las filas del DataFrame
for idx, row in enumerate(df):
    # Filtrar valores NaN
    row = [cell for cell in row if cell is not None]

    # Crear un nuevo grafo para cada fila
    G = nx.Graph()

    # Agregar nodos al grafo G
    for cell in row:
        G.add_node(cell)

    # Agregar conexiones entre nodos en la fila actual
    for i in range(len(row) - 1):
        G.add_edge(row[i], row[i+1])

    # Calcular posiciones de los nodos utilizando el algoritmo spring de NetworkX
    pos = nx.spring_layout(G)

    # Dibujar el gráfico con el tamaño adecuado
    fig, ax = plt.subplots(figsize=figsize)

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
        ax.text(x, y, node, ha='center', va='center')

    # Eliminar ejes
    ax.axis('off')

    # Guardar la figura en un objeto BytesIO
    buf = BytesIO()
    plt.savefig(buf, format='pdf')
    buf.seek(0)

    # Agregar la página PDF al objeto combinador de PDFs
    pdf_merger.append(buf)

    print(f"El diagrama de flujo para la fila {idx+1} se ha generado con éxito ")
    print()

# Guardar el archivo PDF combinado
pdf_combined_file = 'prueba9_diagrama_PDF_combinado.pdf'
with open(pdf_combined_file, 'wb') as output_pdf:
    pdf_merger.write(output_pdf)

print(f"El archivo PDF combinado se ha guardado correctamente en: {pdf_combined_file}")
print()

# Cerrar el libro de Excel y la aplicación de xlwings
wb.close()
app.quit()

