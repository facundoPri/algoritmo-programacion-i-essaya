def factorial(numero):
    resultado = 1
    for i in range(numero):
        resultado = resultado * (i + 1)
    return resultado


def imprimir_factoriales(array):
    for i in array:
        print(factorial(i))


imprimir_factoriales([1, 2, 3, 4, 5])
