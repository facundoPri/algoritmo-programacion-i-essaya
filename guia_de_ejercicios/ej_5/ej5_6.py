def es_potencia_de_dos(numero):
    '''
    Recibe un numero y devuelve si es potencia de dos o no
    '''
    while numero > 1:
        if not numero % 2 == 0:
            return False
        numero = numero // 2
    return True


def sumar_potencias_de_dos_en_rango(indice1, indice2):
    '''
    Recibe dos numeros
    Devuelve la suma de todos los numero que son potencia de dos 
    y estan en el rango de los numeros
    '''
    suma = 0
    for i in range(indice1, indice2):
        if es_potencia_de_dos(i):
            suma += i
    return suma
