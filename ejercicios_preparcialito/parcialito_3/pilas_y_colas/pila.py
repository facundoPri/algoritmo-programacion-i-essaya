class Pila:
    def __init__(self):
        '''
        Inicializa una nueva pila, vacía
        '''
        self._tope = None

    def apilar(self, dato):
        '''
        Agrega un nuevo elemento a la pila
        '''
        nodo = _Nodo(dato, self._tope)
        self._tope = nodo

    def desapilar(self):
        '''
        Desapila el elemento que está en el tope de la pila
        y lo devuelve.
        Pre: la pila NO está vacía.
        Pos: el nuevo tope es el que estaba abajo del tope anterior
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        dato = self._tope.dato
        self._tope = self._tope.prox
        return dato

    def ver_tope(self):
        '''
        Devuelve el elemento que está en el tope de la pila.
        Pre: la pila NO está vacía.
        '''
        if self.esta_vacia():
            raise ValueError("pila vacía")
        return self._tope.dato

    def esta_vacia(self):
        '''
        Devuelve True o False según si la pila está vacía o no
        '''
        return self._tope is None


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
