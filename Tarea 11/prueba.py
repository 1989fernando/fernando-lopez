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
        [22,23,44,25,26,27,28]  # semana 4
    ]
]

# calculamos y mostramos el promedio de temperaturas para cada ciudad por semana
for ciudad in range (ciudades):
    print(f"ciudad {ciudad + 1}:")
    for semana in range (semanas):
        suma_temperaturas=0
        for dia in range (dias):
            suma_temperaturas+=temperaturas[ciudad][semana][dia]
        promedio=suma_temperaturas/dias
        print(f" semana {semana +1}: promedio de temperatura={promedio:.2f}c")
