def definir_aprovados(cantidad_ej, porcentaje_aprov):
    '''
    Recibe como parametros la cantidade de ejercicios de un examen y el procentaje de aprovacion
    Invoca inputs para ingresar examenes
    Devuelve los examenes clasificados
    '''
    examenes = ''
    contador = 0
    ejercicios_aprov = 0
    minimo_aprovacion = (cantidad_ej * porcentaje_aprov)/100
    while ejercicios_aprov != '*':
        contador += 1
        ejercicios_aprov = input('Ingresar candida de ejercicios aprovados: ')
        if ejercicios_aprov == '*':
            break
        if int(ejercicios_aprov) > cantidad_ej:
            print('Cantidad invalida')
            contador -= 1
            continue
        if int(ejercicios_aprov) >= minimo_aprovacion:
            examenes += (str(contador) + 'º examen - Aprovado: ' +
                         str(ejercicios_aprov) + ' / ' + str(cantidad_ej)+'\n')
        elif int(ejercicios_aprov) < minimo_aprovacion:
            examenes += (str(contador) + 'º examen - Desaprovado: ' +
                         str(ejercicios_aprov) + ' / ' + str(cantidad_ej)+'\n')
    return examenes


print(definir_aprovados(13, 62))
