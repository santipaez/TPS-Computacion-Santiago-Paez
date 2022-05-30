#TP 1 Ejercicio 4 - Santiago Páez

n = int(input('Ingrese un número: '))
def diferencia21 (n):
    if n < 21:
        return 21 - n
    else:
        return (21 - n) * 2
print (diferencia21(n))
