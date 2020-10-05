def imprimir_fichas_domino():
    for x in range(7):
        for i in range(x, 7):
            print(x, i, sep=' | ')


imprimir_fichas_domino()
