def calcular_ganancia(pesos, tasa_interes, anios):
    '''
    Calcula la ganancia segun la formula
    recibe como parametros la cantidad de capital inicial en pesos, la tasa de inteses y el numero de anios
    '''
    ganancia = pesos * (1 + tasa_interes/100) ** anios
    return ganancia


def init():
    pesos = float(input('Ingresar pesos: '))
    tasa_interes = float(input('Ingresar tasa de interes: '))
    anios = float(input('Ingresar años: '))
    print(calcular_ganancia(pesos, tasa_interes, anios))


init()
