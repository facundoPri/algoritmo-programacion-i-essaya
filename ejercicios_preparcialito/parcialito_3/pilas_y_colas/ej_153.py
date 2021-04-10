from pila import Pila

def procesar(pila, cadena):
    '''
    Recibe una pila y una cadena
    Efectua una sere de operaciones determinadas por la cadena
    Devuelve la sumatoria de lo que esta en la pila
    '''
    sumatoria = 0
    for caracter in cadena:
        if caracter.isdigit():
            pila.apilar(int(caracter))
        else:
            pila.desapilar()
    while not pila.esta_vacia():
        numero = pila.desapilar()
        sumatoria += numero
    return sumatoria


p = Pila()
cadena = '85x170xx'

print(procesar(p, cadena))
