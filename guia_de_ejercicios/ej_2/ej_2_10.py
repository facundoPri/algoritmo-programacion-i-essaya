def imprimir_fichas_domino(numero):
    for x in range(0, numero+1):
        for i in range(0, numero+1):
            print(x, "|", i)


imprimir_fichas_domino(10)
