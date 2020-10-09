def dia_de_la_semana(dia):
    resto = dia % 7
    nombre_dia = ''

    if resto == 1:
        nombre_dia = 'Lunes'
    elif resto == 2:
        nombre_dia = 'Martes'
    elif resto == 3:
        nombre_dia = 'Miercoles'
    elif resto == 4:
        nombre_dia = 'Jueves'
    elif resto == 5:
        nombre_dia = 'Viernes'
    elif resto == 6:
        nombre_dia = 'Sabado'
    else:
        nombre_dia = 'Domingo'

    return nombre_dia
