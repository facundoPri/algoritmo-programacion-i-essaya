def descomponer_factores_primos(k):
    """
    Recibe un numero k y devuelve la descompocicion en factores primos
    """
    while k > 1:
        for i in range(2, k+1):
            if k % i == 0:
                print(i)
                k = k // i
                break


descomponer_factores_primos(20)
