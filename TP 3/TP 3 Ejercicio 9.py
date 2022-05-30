# Ejercicio 10. Escribir un programa, que reciba una expresión y un archivo e imprima las líneas del archivo que
# contienen la expresión recibida.

import re

def strSearch(search_str,):
    f = open("C:\\Users\\Usr\\PycharmProjects\\SEGUNDO AÑO\\TP 3\\ejercicio9.txt", "r")
    text = f.readlines()
    f.close()
    lines = {}
    for line in text:
        found = re.findall("(" + search_str + ")", line.strip())
        if found:
            line_found = re.sub(r'(' + search_str + ')', r'(\1)', line)
            lines.update({(text.index(line) + 1): line_found})
    if lines:
        print('\nSe han encontrado las siguientes coincidencias:\n')
        for line_num in lines:
            print('Linea %s:\n%s' % (line_num, lines[line_num]))
    else:
        print('No se ha encontrado esa expresión en el archivo.')

search_str = input('Ingrese la expresión a buscar en el archivo: ')
strSearch(search_str)