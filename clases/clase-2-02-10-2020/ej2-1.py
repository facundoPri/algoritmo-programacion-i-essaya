def calcular_ganancia(pesos, tasa_interes, anios):
    '''
    Calcula la ganancia segun la formula
    '''
    return pesos * (1 + tasa_interes/100) ** anios


ganancia = calcular_ganancia(1000, 5, 3)
print(ganancia)
