TAMANIO_DOMINO = 8


def imprimir_fichas(numero):
    for izq in range(numero+1):
        for der in range(izq, numero+1):
            print(izq, der, sep=' - ')


imprimir_fichas(TAMANIO_DOMINO)
