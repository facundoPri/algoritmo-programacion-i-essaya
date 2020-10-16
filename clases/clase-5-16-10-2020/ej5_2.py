def imprimir_descomposicion_primos(k):
    """
    """
    while k > 1:
        for i in range(2, k+1):
            if k % i == 0:
                print(i, end='')
                if k != i:
                    print(' * ', end='')
                k = k // i
                break


imprimir_descomposicion_primos(25)
