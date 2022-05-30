#TP 1 Ejercicio 9 - Santiago Páez

cadena = str(input('Ingrese una palabra: '))
def no_cadena(str):
    if 'no' in str:
        return str
    else:
        str = 'no' + ' ' + str
        return str
print(no_cadena(cadena))
