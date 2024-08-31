# Definimos una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [15, 9, 7],
    [3, 8, 12],
    [14, 10, 5]
]

# Función que ordena una fila específica de la matriz usando Bubble Sort
def ordenar_fila(matriz, fila):
    n = len(matriz[fila])
    for i in range(n):
        for j in range(0, n-i-1):
            if matriz[fila][j] > matriz[fila][j+1]:
                matriz[fila][j], matriz[fila][j+1] = matriz[fila][j+1], matriz[fila][j]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definimos la fila que queremos ordenar (0 para la primera fila, 1 para la segunda, etc.)
fila_a_ordenar = 1

# Ordenamos la fila especificada
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz después de ordenar la fila
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)
