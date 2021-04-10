from lista_enlazada import ListaEnlazada
from cola import Cola

def posicionar_menor_primero(lista):
    menor = lista.prim
    nodo_anterior_menor = None
    nodo_anterior = None
    nodo_actual = lista.prim
    while nodo_actual:
        if nodo_actual.dato < menor.dato and not menor == lista.prim:
            nodo_anterior_menor.prox = menor
            nodo_anterior.prox = nodo_actual.prox
            menor = nodo_anterior
            nodo_anterior_menor = nodo_anterior
        nodo_actual = nodo_actual.prox
    menor.prox = lista.prim
    lista.prim = menor


class ColaDistribuidora:
    def __init__(self, ids, f):
        self.f = f
        self.ids = ids
        self.colas = {}

    def encolar(self, elemento):
        resultado, id = self.f(elemento)
        self.colas[id] = self.colas.get(id, Cola())
        self.colas[id].encolar(resultado)

    def desencolar(self, id):
        if not self.colas.get(id, False):
            raise ValueError("El identificador pasado no corresponde")
        return self.colas[id].desencolar()

    def esta_vacia(self):
        for id in self.ids:
            if not self.colas.get(id, False):
                continue
            if not self.colas[id].esta_vacia():
                return False
        return True


"""
Caso A: Posible
- paso1 * 5
- paso2 * 2
- paso3 * 2
- paso2
- paso3
- paso2 * 2
- paso3 * 2

Caso B: Imposible
"""
