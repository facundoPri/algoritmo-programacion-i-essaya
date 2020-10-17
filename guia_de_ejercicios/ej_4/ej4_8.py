def dias_mes(dia, mes):
    '''
    Recibe el dia y el mes y devuelve un aproximado de los dias que pasaron del anio
    '''
    return (mes - 1) * 30 + dia


def devolver_signo(dia, mes):
    """
    Recibe el dia y mes de tu cumpleanos y te devuelve el signo
    """
    dias = dias_mes(dia, mes)
    if dias > 360:
        return 'Fecha invalida'
    elif dias >= dias_mes(22, 12) or dias <= dias_mes(20, 1):
        return 'Capricornio'
    elif dias_mes(21, 1) <= dias <= dias_mes(19, 2):
        return 'Acuario'
    elif dias_mes(20, 2) <= dias <= dias_mes(20, 3):
        return 'Piscis'
    elif dias_mes(21, 3) <= dias <= dias_mes(20, 4):
        return 'Aries'
    elif dias_mes(21, 4) <= dias <= dias_mes(20, 5):
        return 'Tauro'
    elif dias_mes(21, 5) <= dias <= dias_mes(21, 6):
        return 'Geminis'
    elif dias_mes(22, 6) <= dias <= dias_mes(23, 7):
        return 'Cancer'
    elif dias_mes(24, 7) <= dias <= dias_mes(23, 8):
        return 'Leo'
    elif dias_mes(24, 8) <= dias <= dias_mes(23, 9):
        return 'Virgo'
    elif dias_mes(24, 9) <= dias <= dias_mes(22, 10):
        return 'Libra'
    elif dias_mes(23, 10) <= dias <= dias_mes(22, 11):
        return 'Escorpio'
    elif dias_mes(23, 11) <= dias <= dias_mes(21, 12):
        return 'Sagitario'


def main():
    """
    Funcion main, ejecuta dos inputs preguntando el mes y el dia de nacimiento
    Devuelve el signo de la persona
    """
    dia = int(input('Igresar dia de nacimiento: '))
    mes = int(input('Igresar mes de nacimiento: '))
    print(devolver_signo(dia, mes))


main()
