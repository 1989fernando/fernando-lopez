# Creación y escritura de un archivo de texto llamado "my_notes.txt"
# Este archivo contendrá al menos tres líneas de notas personales.

# Abrimos el archivo en modo de escritura ('w') y escribimos las notas
with open("my_notes.txt", "w") as file:
    # Escribimos las notas personales en el archivo
    file.write("Primera nota: Recordar revisar el correo.\n")
    file.write("Segunda nota: Comprar ingredientes para la cena.\n")
    file.write("Tercera nota: Leer el capítulo 4 del libro.\n")

# Ahora, abrimos el archivo para leer su contenido línea por línea y mostrarlo en la consola
# Abrimos el archivo en modo de lectura ('r')
with open("my_notes.txt", "r") as file:
    # Leemos y mostramos cada línea del archivo
    line = file.readline()  # Lee la primera línea
    while line:
        print(line.strip())  # Mostramos la línea sin saltos de línea adicionales
        line = file.readline()  # Lee la siguiente línea

# Después de leer, el archivo se cierra automáticamente gracias al uso del "with" statement.
