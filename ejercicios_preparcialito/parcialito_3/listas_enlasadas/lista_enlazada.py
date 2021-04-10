class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.cant = 0

    def append(self, dato):
        nuevo = _Nodo(dato)
        if not self.prim:
            self.prim = nuevo
        else:
            act = self.prim
            while act.prox:
                act = act.prox
            # act es el ultimo nodo
            act.prox = nuevo
        self.cant += 1

    def show(self):
        nodo = self.prim
        while nodo:
            print(nodo.dato)
            nodo = nodo.prox

    def __len__(self):
        return self.cant


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
