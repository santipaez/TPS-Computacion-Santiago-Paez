#TP 1 Ejercicio 5 - Santiago Páez


hablando = input('¿El loro está hablando? Si/No: ')
hora = int(input('¿Qué hora es?: '))
def problema_loro(hablando, hora):
    if hablando == 'Si':
        hablando = True
    elif hablando == 'No':
        hablando = False
    else:
        print(hablando, 'no es una respuesta correcta. Indique Si/No')
    if hora > 23:
       print (hora, 'no es una respuesta correcta. Indique la hora de 0 a 23.')
    if hablando is True and hora > 0 and hora < 7:
       return True
    if hablando is True and hora > 20 and hora < 24:
       return True
    else:
       return False
print(problema_loro(hablando, hora))
