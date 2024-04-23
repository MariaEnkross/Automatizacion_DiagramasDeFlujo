import random
import string 

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