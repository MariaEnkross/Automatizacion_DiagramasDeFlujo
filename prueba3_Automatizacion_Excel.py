import openpyxl
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

# Abre el archivo Excel
wb = openpyxl.load_workbook('Agenda_Tareas.xlsx')
sheet = wb.active  # O accede a una hoja específica si es necesario

# Leer datos de la hoja Excel y almacenarlos en una lista
data = []
for row in sheet.iter_rows(values_only=True):
    data.append(row)

# Crear un documento PDF
pdf_filename = "prueba3_datos_excel.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=letter)

# Crear una tabla con los datos
table = Table(data)

# Aplicar estilo a la tabla
style = TableStyle([('BACKGROUND', (0,0), (-1,0), colors.grey),
                    ('TEXTCOLOR',(0,0),(-1,0),colors.whitesmoke),
                    ('ALIGN', (0,0), (-1,-1), 'CENTER'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                    ('BOTTOMPADDING', (0,0), (-1,0), 12),
                    ('BACKGROUND',(0,1),(-1,-1),colors.beige),
                    ('GRID',(0,0),(-1,-1),1,colors.black)])
table.setStyle(style)

# Agregar la tabla al documento PDF
elements = [table]
doc.build(elements)

print(f"El PDF ha sido generado correctamente con el nombre: '{pdf_filename}'")

