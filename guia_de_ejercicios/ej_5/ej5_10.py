def es_primo(numero):
    '''
    Recibe un numero
    Devuele si es primo o no
    '''
    primo = True
    if numero == 1:
        primo = False
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
    return primo


def imprimir_numero_primos_hasta(numero):
    for i in range(1, numero):
        if es_primo(i):
            print(i)


imprimir_numero_primos_hasta(100)
