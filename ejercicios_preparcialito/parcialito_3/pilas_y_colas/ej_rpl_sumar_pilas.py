from cola import Cola
from pila import Pila


def sumar_pilas(pila1, pila2):
    """
    DOC: Completar
    """
    pila1_invertida = Pila()
    pila2_invertida = Pila()
    pila_final = Pila()
    while not pila1.esta_vacia() or not pila2.esta_vacia():
        n1 = pila1.desapilar() if not pila1.esta_vacia() else 0
        n2 = pila2.desapilar() if not pila2.esta_vacia() else 0
        pila1_invertida.apilar(n1) if not n1 == 0 else None
        pila2_invertida.apilar(n2) if not n2 == 0 else None
    while not pila1_invertida.esta_vacia or not pila2_invertida.esta_vacia():
        numero_anterior = pila_final.desapilar() if not pila_final.esta_vacia() else 0
        n1 = pila1_invertida.desapilar() if not pila1_invertida.esta_vacia() else 0
        n2 = pila2_invertida.desapilar() if not pila2_invertida.esta_vacia() else 0
        print(n1, n2)
        suma = n1 + n2
        suma += numero_anterior
        proximo_numero = suma // 10
        suma = suma % 10
        pila_final.apilar(suma)
        pila_final.apilar(proximo_numero) if not proximo_numero == 0 else None

    return pila_final


p1 = Pila()
p2 = Pila()

p1.apilar(9)
p1.apilar(1)
p1.apilar(1)

p2.apilar(9)
p2.apilar(9)
p2.apilar(9)
p2.apilar(9)

pf = sumar_pilas(p1, p2)
