def es_bisiesto(anio):
    if anio % 4 != 0:
        return False

    return not(anio % 100 == 0 and anio % 400 != 0)


print('es_bisiesto(2020): ', es_bisiesto(2020))
