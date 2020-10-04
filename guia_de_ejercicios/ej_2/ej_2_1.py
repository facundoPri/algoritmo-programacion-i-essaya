def calcular_ganancia(pesos, tasa_interes, anios):
    '''
    Calcula la ganancia segun la formula
    recibe como parametros la cantidad de capital inicial en pesos, la tasa de inteses y el numero de anios
    '''
    ganancia = pesos * (1 + tasa_interes/100) ** anios
    return ganancia


print(calcular_ganancia(100, 2, 10))
