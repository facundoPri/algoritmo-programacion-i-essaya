def imprimir_fichas():
    for izq in range(7):
        for der in range(izq, 7):
            print(izq, der, sep=' - ')


imprimir_fichas()
