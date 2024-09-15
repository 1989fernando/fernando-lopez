# definimos las dimenciones de la matriz
ciudades= 3 # numeros de ciudades
dias= 7     # dias de la semana
semanas =4  # numeros de semana
# creamos una matriz 3D para almacenar datos
temperaturas = [
    [ # ciudad 1
        [28,41,40,38,27,36,25], # semana 1
        [40,42,21,29,38,27,26], # semana 2
        [41,43,42,30,39,28,27], # semana 3
        [32,24,23,41,40,39,28]  # semana 4
    ],
    [ # ciudad 2
        [44,35,36,27,48,29,30], # semana 1
        [25,46,47,38,39,30,31], # semana 2
        [26,37,38,39,40,41,32], # semana 3
        [27,38,39,40,41,42,33]  # semana 4
    ],
    [ # ciudad 3
        [39,40,21,42,23,34,25], # semana 1
        [40,21,22,43,24,35,26], # semana 2
        [21,22,23,44,25,36,27], # semana 3
        [22,23,44,25,26,27,28], # semana 4
],


def calcular_promedio_temperaturas(ciudades_temperaturas):
    """
    Calcula el promedio de temperatura para cada ciudad durante el período dado.

    Parámetros:
    ciudades_temperaturas (dict): Un diccionario donde las claves son los nombres de las ciudades
                                  y los valores son listas de listas que contienen las temperaturas
                                  por semana para cada ciudad.

    Retorna:
    dict: Un diccionario con las ciudades y sus respectivas temperaturas promedio.
    """
    promedios = {}

    for ciudad, semanas in ciudades_temperaturas.items():
        # Aplanar la lista de semanas en una sola lista de temperaturas
        todas_temperaturas = [temp for semana in semanas for temp in semana]

        # Calcular el promedio
        if len(todas_temperaturas) > 0:
            promedio = sum(todas_temperaturas) / len(todas_temperaturas)
        else:
            promedio = 0

        # Guardar el resultado
        promedios[ciudad] = promedio

    return promedios


# Ejemplo de uso
ciudades_temperaturas = {
    "Ciudad A": [[30, 32, 33], [31, 29, 34], [28, 30, 32]],  # 3 semanas de temperaturas
    "Ciudad B": [[20, 21, 22], [23, 22, 21], [24, 23, 22]],
    "Ciudad C": [[15, 14, 16], [15, 17, 16], [14, 15, 16]],
}

promedios = calcular_promedio_temperaturas(ciudades_temperaturas)
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperatura en {ciudad} es {promedio:.2f}°C")
