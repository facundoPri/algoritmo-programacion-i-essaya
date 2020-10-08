def calcular_tiempo_a_segundos(horas=0, minutos=0, segundos=0):
    '''
    Recibo cantidad de horas, minutos y segundos y devuelvo el equivalente a eso en apenas segundos
    '''
    return horas * 60 * 60 + minutos * 60 + segundos


print('a-')
print(calcular_tiempo_a_segundos(2, 10, 10))


def calcular_segundos_a_tiempo(seg=0):
    '''
    Recibo una cantidad de segundo y devuelvo el equivalente en horas, minutos y segundos
    '''
    horas = seg // 3600
    minutos = (seg % 3600) // 60
    segundos = (seg % 3600) % 60
    return horas, minutos, segundos


print('')
print('b-')
print(calcular_segundos_a_tiempo(7810))
