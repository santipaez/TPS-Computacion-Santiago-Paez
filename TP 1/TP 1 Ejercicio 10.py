#TP 1 Ejercicio 10 - Santiago Páez

palabra = str(input('Ingrese una palabra: '))
num = int(input('Ingrese el índice: '))
def carácter_perdido(str, n):
    if n or n == 0:
        mitad1 = str [:n]
        mitad2 = str[n+1:]
        return mitad1 + mitad2
    elif n == -1:
        return str[:-1]
print (carácter_perdido(palabra, num))
