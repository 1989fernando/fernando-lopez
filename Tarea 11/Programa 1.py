# Definimos una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [5, 8, 12],
    [9, 15, 7],
    [3, 14, 10]
]

# Función que busca un valor específico en la matriz
def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return f"Valor {valor} encontrado en la posición ({i}, {j})"
    return f"Valor {valor} no encontrado en la matriz"

# Definimos el valor a buscar
valor_a_buscar = 15

# Llamamos a la función y mostramos el resultado
resultado = buscar_valor(matriz, valor_a_buscar)
print(resultado)
