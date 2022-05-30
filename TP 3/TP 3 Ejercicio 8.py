# Ejercicio 8. Escribir un programa, que reciba un archivo, lo procese e imprima por pantalla cuántas líneas, cuantas
# palabras y cuántos caracteres contiene el archivo.

file = open("ejercicio8.txt", 'r')
texto = file.read()

def contar_caracteres(cadena):
    numeros = 0
    letras = 0
    for c in cadena:
        if c.isdigit():
            numeros += 1
        elif c.isalpha():
            letras += 1
        else:
            pass
    return numeros, letras

with open('ejercicio8.txt') as myfile:
    contar_lineas = sum(1 for line in myfile)

contar_palabras = len(texto.split())

print('Cantidad de lineas: %i' % contar_lineas)
print('Cantidad de palabras: %i' % contar_palabras)
print('Cantidad de caracteres: %i' % contar_caracteres(texto)[1])








