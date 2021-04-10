class Cola:
    '''Representa a una cola, con operaciones de encolar y
       desencolar. El primero en ser encolado es también el primero
       en ser desencolado.'''

    def __init__(self):
        '''Crea una cola vacía'''
        self._frente = None
        self._ultimo = None

    def encolar(self, dato):
        '''Agrega el elemento x como último de la cola.'''
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self._frente = nodo
        else:
            self._ultimo.prox = nodo
        self._ultimo = nodo

    def desencolar(self):
        '''Desencola el primer elemento y devuelve su valor
           Pre: la cola NO está vacía.
           Pos: el nuevo frente es el que estaba siguiente al frente anterior'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        dato = self._frente.dato
        self._frente = self._frente.prox
        if self._frente is None:
            self._ultimo = None
        return dato

    def ver_frente(self):
        '''Devuelve el elemento que está en el frente de la cola.
           Pre: la cola NO está vacía.'''
        if self.esta_vacia():
            raise ValueError("Cola vacía")
        return self._frente.dato

    def esta_vacia(self):
        '''Devuelve True o False según si la cola está vacía o no'''
        return self._frente is None


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
