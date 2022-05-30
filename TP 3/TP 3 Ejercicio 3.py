# Ejercicio 3. Escribir un programa, para agregar texto a un archivo y mostrar el texto.

f = open('ejercicio3.txt','w')
f.write(str(input('Ingresar texto para agregar: ')))
f = open('ejercicio3.txt','r')
print (f.read())