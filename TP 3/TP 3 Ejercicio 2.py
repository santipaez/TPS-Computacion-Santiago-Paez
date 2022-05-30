# Ejercicio 2. Escribir un programa, para leer las primeras n líneas de un archivo.

from itertools import islice

n = int (input('Ingrese las primeras N lineas a leer: '))

with open('ejercicio2y6.txt', 'r') as f:
  for l in islice(f,n):
    print (l, end='')