
# Crear diccionario con información ficticia
informacion_personal = {
    "nombre": "Ana Gómez",
    "edad": 30,
    "ciudad": "Madrid",
    "profesion": "Ingeniera"
}

# Modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Barcelona"

# Agregar nueva clave-valor "profesion"
informacion_personal["profesion"] = "Desarrolladora de software"

# Verificar si la clave "telefono" existe; si no, agregarla
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "123-456-789"

# Eliminar la clave "edad"
informacion_personal.pop("edad", None)

# Imprimir el diccionario final
informacion_personal
