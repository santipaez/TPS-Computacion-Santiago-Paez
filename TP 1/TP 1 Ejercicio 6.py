#TP 1 Ejercicio 6 - Santiago Páez

a = int(input('Ingrese el número A: '))
b = int(input('Ingrese el número B: '))
def hacer10 (a, b):
    if a == 10 or b == 10:
        return True
    elif (a + b) == 10:
        return True
    else:
        return False
print(hacer10(a, b))
