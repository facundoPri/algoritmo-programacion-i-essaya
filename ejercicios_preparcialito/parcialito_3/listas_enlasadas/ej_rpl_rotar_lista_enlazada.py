def rotar(self, N):
    '''
    DOC: Completar
    '''
    if N == self.cant + 1 or self.cant == 0:
        return
    primer_nodo = self.prim
    nodo_actual = primer_nodo
    for index in range(self.cant - 1):
        if index == N:
            siguiente_nodo = nodo_actual.prox
            nodo_actual.prox = None
            nodo_actual = siguiente_nodo
            self.prim = nodo_actual
        else:
            nodo_actual = nodo_actual.prox
    nodo_actual.prox = primer_nodo
