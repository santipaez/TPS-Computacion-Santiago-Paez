# Ejercicio 5. Escribir un programa, para copiar el contenido de un archivo a otro archivo.

with open('ejercicio5A.txt', 'r') as firstfile, open('ejercicio5B.txt', 'w') as secondfile:
    for line in firstfile:
        secondfile.write(line)