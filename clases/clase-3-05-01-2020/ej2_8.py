def calcular_factorial(numero):
    '''
    '''
    resultado = 1
    for i in range(2, numero+1):
        resultado *= i
    return resultado


def imprimir_factoriales(cantidad):
    '''
    '''
    for i in range(cantidad):
        numero = int(input('Ingrese el numero a calcular: '))
        print(i+1, calcular_factorial(numero), sep=' - ')


imprimir_factoriales(3)
