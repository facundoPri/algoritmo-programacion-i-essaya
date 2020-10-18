def imprimir_numeros_multipos_for(numero1, numero2):
    '''
    Recibe dos numeros
    Devuelve la cantidad de multimos del numero1 menores al numero dos
    '''
    contador = 0
    for i in range(numero1, numero2):
        if i % numero1 == 0:
            contador += 1
    print(contador)


def imprimir_numeros_multipos_while(numero1, numero2):
    '''
    Recibe dos numeros
    Devuelve la cantidad de multimos del numero1 menores al numero dos
    '''
    contador = 0
    i = 1
    while i < numero2:
        if i % numero1 == 0:
            contador += 1
        i += 1
    print(contador)


imprimir_numeros_multipos_while(1, 50)
