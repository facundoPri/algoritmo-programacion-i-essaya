def calcular_ganancia(pesos, tasa_interes, anios):
    '''
    Calcula la ganancia segun la formula
    '''
    return pesos * (1 + tasa_interes/100) ** anios


def main():
    '''
    Llamo 3 input para recibir los valores de pesos tasa_interes y anios
    imprime en pantalla el resultado calculado por la funcion calcular_ganancia
    '''
    pesos = float(input('Ingrese una cantidad de pesos: '))
    tasa_interes = float(input('Ingrese tasa de interes: '))
    anios = float(input('Ingrese cant de anios: '))
    print(calcular_ganancia(pesos, tasa_interes, anios))


main()
