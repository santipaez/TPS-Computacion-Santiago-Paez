# Ejercicio 6. Escribir un programa, que reciba un archivo y un número N e imprima las primeras N líneas del archivo.

from itertools import islice

n = int(input('Ingrese las primeras N lineas a leer: '))

with open('ejercicio2y6.txt', 'r') as f:
  for l in islice(f,n):
    print (l, end='')

