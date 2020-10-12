def dia_semana_anio(dia):
    """
    Recibe un dia de 1 a 366
    Devuelve el dia de la semana correspondiente siendo lunes primer dia de la semana
    """
    resto = dia % 7
    if resto == 1:
        return 'Lunes'
    elif resto == 2:
        return 'Martes'
    elif resto == 3:
        return 'Miercoles'
    elif resto == 4:
        return 'Jueves'
    elif resto == 5:
        return 'Viernes'
    elif resto == 6:
        return 'Sabado'
    else:
        return 'Domingo'
