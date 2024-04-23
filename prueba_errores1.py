import matplotlib.pyplot as plt
import numpy as np

vector=["IME1","W1","IME2","W2","IME3"]
grafo=vector[:]
tam=len(vector)
#cuenta de la línea dentro de la página
linea=0
for i in range(tam):
		grafo[i]=str(vector[i]) + ", [" + str(i*10) + ","+ str(linea)+"],"
print(grafo)
