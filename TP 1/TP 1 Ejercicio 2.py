#TP 1 Ejercicio 2 - Santiago Páez

a_sonriendo = input('¿El mono A está sonriendo?: Si/No: ')
b_sonriendo = input('¿El mono B está sonriendo?: Si/No: ')
def problemas_monos(a_sonriendo, b_sonriendo):
    if a_sonriendo == 'Si':
        a_sonriendo = True
    elif a_sonriendo == 'No':
        a_sonriendo = False
    else:
        print(a_sonriendo, 'no es una respuesta correcta. Indique Si/No')
    if b_sonriendo == 'Si':
        b_sonriendo = True
    elif b_sonriendo == 'No':
        b_sonriendo = False
    else:
        print(b_sonriendo, 'no es una respuesta correcta. Indique Si/No')
    if a_sonriendo is True and b_sonriendo is False:
        return False
    if a_sonriendo is False and b_sonriendo is False:
        return True
    if a_sonriendo is True and b_sonriendo is True:
        return True
    else:
        return False
print (problemas_monos(a_sonriendo, b_sonriendo))
