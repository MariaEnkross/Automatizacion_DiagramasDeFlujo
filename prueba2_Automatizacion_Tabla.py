import random
import string 
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib.pagesizes import landscape, A3, A4

# Define the dimensions of the matrix
rows = 5
cols = 3
 
# Create an empty matrix
matrix = []
 
# Use a loop to populate the first row with random characters between 'a' and 'z'
first_row = [random.choice(string.ascii_lowercase + string.digits +  string.ascii_uppercase) for _ in range(cols)]
 
# Append the first row to the matrix
matrix.append(first_row)
 
# Use nested loops to populate the remaining rows with random numbers between 1 and 9
for i in range(1, rows):
    row = []  # Create an empty row
    for j in range(cols):
        row.append(random.randint(1, 10))  # Append a random number between 1 and 9 to each column in the row
    matrix.append(row)  # Append the row to the matrix
 
# Print the matrix
print (matrix)

# Salto de línea
print("")

# Print the matrix (ordenada)
for row in matrix:
    print(row)

# Salto de línea
print (" ")

# Print valores
print("El primer valor importado es el:", matrix[0][0])
print("El último valor importado es el:", matrix[rows-1][cols-1])

# Crear un documento PDF
pdf_filename = "prueba2_tablaPDF.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

# Convertir la matriz en una tabla para el PDF
data = [['' for _ in range(cols)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols):
        data[i][j] = str(matrix[i][j])

# Crear la tabla
table = Table(data)

# Estilo de la tabla
style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 12),
                    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                    ('GRID',(0,0),(-1,-1),1,colors.black)])

table.setStyle(style)

# Crear los elementos del PDF
elements = [table]

# Generar el PDF
doc.build(elements)

print(f"El PDF ha sido generado correctamente")
