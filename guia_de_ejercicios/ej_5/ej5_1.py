def calcular_promedio():
    suma_notas = 0
    cant_notas = 0
    seguir = 'S'
    while not seguir == 'n':
        suma_notas += float(input('Ingresar nota: '))
        cant_notas += 1

        seguir = input('Desea ingresar mas notas:[S/n] ')

    return suma_notas/cant_notas


def main():
    '''
    Ejecuta la funcion calcular_promedio y la imprime
    '''
    print(calcular_promedio())


main()
