#TP 1 Ejercicio 8 - Santiago Páez

a = int(input('Ingrese el número A: '))
b = int(input('Ingrese el número B: '))
negativa = input('¿El parámetro negativo es verdadero o falso?: V/F: ')
if negativa == 'V':
    negativa = True
elif negativa == 'F':
    negativa = False
else:
    print ('La respuesta no es la correcta, indique V o F.')
def pos_negativa(a, b, negativa):
    if a < 0 and b < 0 and negativa is True:
        return True
    if a > 0 and b < 0 and negativa is False:
        return True
    elif a < 0 and b > 0 and negativa is False:
        return True
    else:
        return False
print (pos_negativa(a, b, negativa))
