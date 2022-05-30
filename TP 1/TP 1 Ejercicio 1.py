#TP 1 Ejercicio 1 - Santiago Páez

dia_semana = ['Lunes','Martes','Miercoles','Jueves','Viernes']
vacaciones = 'Vacaciones'
dia = input('Ingrese el dia de la semana, en caso de vacaciones: "Vacaciones": ')
if dia not in vacaciones and dia not in dia_semana and dia != 'Sabado' and 'Domingo':
    print(dia, 'no es un día de la semana.Por favor, ingrese otro día.')
def dormimos(dia_semana, vacaciones, dia):
    if dia in vacaciones:
        return True
    if dia not in dia_semana:
        return True
    if dia in dia_semana:
        return False
print (dormimos(dia_semana, vacaciones, dia))
