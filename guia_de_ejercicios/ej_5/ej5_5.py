def calcular_mcd(n, m):
    '''
    Recibe dos numeros y le aplica el alforitmo de euclides para obtener el maximos comun divisor
    '''

    while True:
        r = m % n
        if r == 0:
            return n
        m = n
        n = r


assert calcular_mcd(15, 9) == 3
assert calcular_mcd(9, 15) == 3
assert calcular_mcd(10, 8) == 2
assert calcular_mcd(12, 6) == 6
