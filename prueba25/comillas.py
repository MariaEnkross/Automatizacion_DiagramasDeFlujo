## Formato texto ##
for row in range(1, sheet.max_row + 1):
    # Columna A
    value_column_A = sheet.cell(row=row, column=1).value
    if value_column_A and isinstance(value_column_A, str) and value_column_A.startswith('=') and sheet.cell(row=row, column=1).data_type != 'f':
        sheet.cell(row=row, column=1).value = '=TEXTO("' + value_column_A + '","@")'
    
    # Columna K
    value_column_K = sheet.cell(row=row, column=11).value
    if value_column_K and isinstance(value_column_K, str) and value_column_K.startswith('=') and sheet.cell(row=row, column=11).data_type != 'f':
        sheet.cell(row=row, column=11).value = '=TEXTO("' + value_column_K + '","@")'
    
    # Columna L
    value_column_L = sheet.cell(row=row, column=12).value
    if value_column_L and isinstance(value_column_L, str) and value_column_L.startswith('=') and sheet.cell(row=row, column=12).data_type != 'f':
        sheet.cell(row=row, column=12).value = '=TEXTO("' + value_column_L + '","@")'


## Borrar primero y luego añadir ##
for row in range(1, sheet.max_row + 1):
    # Columna A
    value_column_A = sheet.cell(row=row, column=1).value
    if value_column_A and isinstance(value_column_A, str) and value_column_A.startswith('=') and sheet.cell(row=row, column=1).data_type != 'f':
        if value_column_A.startswith("'"):
            value_column_A = value_column_A[1:]  # Eliminar la comilla simple existente
        sheet.cell(row=row, column=1).value = "'" + value_column_A
    
    # Columna K
    value_column_K = sheet.cell(row=row, column=11).value
    if value_column_K and isinstance(value_column_K, str) and value_column_K.startswith('=') and sheet.cell(row=row, column=11).data_type != 'f':
        if value_column_K.startswith("'"):
            value_column_K = value_column_K[1:]  # Eliminar la comilla simple existente
        sheet.cell(row=row, column=11).value = "'" + value_column_K
    
    # Columna L
    value_column_L = sheet.cell(row=row, column=12).value
    if value_column_L and isinstance(value_column_L, str) and value_column_L.startswith('=') and sheet.cell(row=row, column=12).data_type != 'f':
        if value_column_L.startswith("'"):
            value_column_L = value_column_L[1:]  # Eliminar la comilla simple existente
        sheet.cell(row=row, column=12).value = "'" + value_column_L


## Verificar si el valor ya contiene una comilla simple al principio ##
for row in range(1, sheet.max_row + 1):
    # Columna A
    value_column_A = sheet.cell(row=row, column=1).value
    if value_column_A and isinstance(value_column_A, str) and value_column_A.startswith('='):
        if not value_column_A.startswith("'"):
            sheet.cell(row=row, column=1).value = "'" + value_column_A
    
    # Columna K
    value_column_K = sheet.cell(row=row, column=11).value
    if value_column_K and isinstance(value_column_K, str) and value_column_K.startswith('='):
        if not value_column_K.startswith("'"):
            sheet.cell(row=row, column=11).value = "'" + value_column_K
    
    # Columna L
    value_column_L = sheet.cell(row=row, column=12).value
    if value_column_L and isinstance(value_column_L, str) and value_column_L.startswith('='):
        if not value_column_L.startswith("'"):
            sheet.cell(row=row, column=12).value = "'" + value_column_L
