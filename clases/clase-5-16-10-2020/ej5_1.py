def calcular_promedio_notas():
    '''
    Le preguntamos al usuario notas y busca su promedio
    '''

    cant_notas = 0
    suma_notas = 0

    while True:
        nota = float(input('Ingrese la nota: '))

        if not 0 <= nota <= 10:
            continue

        suma_notas += nota
        cant_notas += 1

        opc = input('Desea ingresar mas notas? [Y/n]: ')
        if opc == 'n':
            break

    print('Su promedio: ', suma_notas/cant_notas)


calcular_promedio_notas()
