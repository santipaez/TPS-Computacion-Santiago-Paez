#TP 1 Ejercicio 7 - Santiago Páez

n = int(input('Ingrese un número: '))
def cerca_cien(n):
    if 90 <= n <= 110:
        return True
    elif 190 <= n <= 210:
        return True
    else:
        return False
print(cerca_cien(n))
