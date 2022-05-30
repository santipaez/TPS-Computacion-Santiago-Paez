# Ejercicio 4. Escribir un programa, para leer un archivo línea por línea y almacenarlo en una lista.

lista = []
fichero = open('ejercicio4.txt','r')
lineas = fichero.readlines()
lista.append(lineas)
print (lista)