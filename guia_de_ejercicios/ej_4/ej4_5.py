def indicar_anio_bisiesto(anio):
    """
    Recibe un anio y devuelve si es bisiesto o no
    """
    if not anio % 4 == 0:
        return False
    return not (anio % 100 == 0 and not anio % 400 == 0)


def indicar_cantidad_dias_mes(mes, anio):
    """
    Recibe un mes y un anio y nos devuelve la cantidad de dias de ese mes
    """
    mes_resto = mes % 12
    if mes_resto == 2:
        if indicar_anio_bisiesto(anio):
            return 29
        else:
            return 28
    if mes_resto % 2 == 0:
        return 30
    else:
        return 31


def validar_fecha(dia, mes, anio):
    """
    Recibe dia, mes y anio como parametro
    Devuelve si la fecha es valida o no
    """
    return dia <= indicar_cantidad_dias_mes(mes, anio) and mes < 12


def indicar_dias_faltantes_fin_mes(dia, mes, anio):
    """
    Recibe una fecha
    Devuelve cuanto falta para el fin del mes
    """
    if not validar_fecha(dia, mes, anio):
        return 'Fecha Invalida'
    return indicar_cantidad_dias_mes(mes, anio) - dia


def indicar_dias_faltantes_fin_anio(dia, mes, anio):
    """
    Recibe una fecha
    Devuelve cuanto falta para fin de anio
    """
    if not validar_fecha(dia, mes, anio):
        return 'Fecha Invalida'
    dias = 0
    for i in range(mes, 13):
        dias += indicar_cantidad_dias_mes(i, anio)
    return dias - dia + 1


def indicar_cuantos_dias_pasaron_en_anio(dia, mes, anio):
    """
    Recibe una fecha
    Devuelve cuantos dias pasaron del anio
    """
    if not validar_fecha(dia, mes, anio):
        return 'Fecha Invalida'
    dias = 0
    for i in range(1, mes):
        dias += indicar_cantidad_dias_mes(i, anio)
    return dia + dias


def tiempo_transcurrido(dia1, mes1, anio1, dia2, mes2, anio2):
    """
    Recibe dos fechas y devuelve el tiempo trascurrido entre ellos
    """
    if not validar_fecha(dia1, mes1, anio1) and not validar_fecha(dia2, mes2, anio2):
        return 'Fechas invalidas'
    dias = 0
    meses = mes2 - mes1
    anios = anio2 - anio1
    if anios != 0:
        dias += indicar_dias_faltantes_fin_anio(dia1, mes1, anio1)
        dias += indicar_cuantos_dias_pasaron_en_anio(dia2, mes2, anio2)
        dias += 365 * (anios-1)
    elif meses != 0:
        dias += indicar_dias_faltantes_fin_mes(dia1, mes1, anio1)
        dias += dia2 + 1
        dias += 30 * (meses - 1)
    elif meses == 0:
        dias = dia1 - dia2

    return dias // 365, (dias % 365)//30, (dias % 365) % 30


print(tiempo_transcurrido(5, 7, 2013, 7, 9, 2013))
print(tiempo_transcurrido(23, 8, 2014, 11, 4, 2015))
print(tiempo_transcurrido(5, 9, 2011, 31, 1, 2013))
