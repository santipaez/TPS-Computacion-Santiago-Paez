#TP 1 Ejercicio 3 - Santiago Páez

a = int(input('Ingrese el número A: '))
b= int(input('Ingrese el número B: '))
def suma_doble(a, b):
    if a == b:
        return 2 * (a + b)
    else:
        return a + b
print (suma_doble(a, b))
