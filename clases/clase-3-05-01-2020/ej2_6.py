def imprimir_pares_rango(inicio, final):
    '''
    '''
    for i in range(inicio + inicio % 2, final, 2):
        print(i)


def pedir_numeros():
    '''
    '''
    primero = int(input('Escribo el primer numero: '))
    segundo = int(input('Escribo el segundo numero: '))
    return primero, segundo  # devuelve una tupla


def main():
    '''
    '''
    # inicio, final = pedir_numeros()
    # imprimir_pares_rango(inicio, final)

    # el * es una forma de desestructurar la tupla que devuelve la funcion
    imprimir_pares_rango(*pedir_numeros())


main()
