def sumar_divisores(numero):
    """
    Recibe un numero
    Devuelve la suma de todos sus numeros divisores
    """
    suma = 0
    for i in range(1, numero):
        if numero % i == 0:
            suma += i
    return suma


def listar_numeros_perfectos(cantidad):
    '''
    Recibe una cantidad
    Devuelve una lista de numeros perfectos con la cantidad pasada
    '''
    numero = 1
    while cantidad > 0:
        if sumar_divisores(numero) == numero:
            cantidad -= 1
            print(sumar_divisores(numero))
        numero += 1


def listar_numeros_amigos(cantidad):
    """
    Recibe una cantidad
    Devuelve una lista de numeros amigos con la cantidad pasada
    """
    a = 1
    b = 1
    ultimo_b = 1
    while cantidad > 0:
        b = sumar_divisores(a)
        if a == sumar_divisores(b) and not a == b and not a == ultimo_b:
            print(a, b)
            ultimo_b = b
            cantidad -= 1
        a += 1


listar_numeros_amigos(10)
