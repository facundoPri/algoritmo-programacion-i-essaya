class ListaEnlazada:
    def __init__(self):
        # prim es un _Nodo o None
        self.prim = None
        self.len = 0

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
        self.len += 1

    def pop(self, i=None):
        """Elimina el nodo de la posición i, y devuelve el dato contenido.
        Si i está fuera de rango, se levanta la excepción IndexError.
        Si no se recibe la posición, devuelve el último elemento."""

        if i is None:
            i = self.len - 1

        if i < 0 or i >= self.len:
            raise IndexError("Índice fuera de rango")

        if i == 0:
            # Caso particular: saltear la cabecera de la lista
            dato = self.prim.dato
            self.prim = self.prim.prox
        else:
            # Buscar los nodos en las posiciones (i-1) e (i)
            n_ant = self.prim
            n_act = n_ant.prox
            for pos in range(1, i):
                n_ant = n_act
                n_act = n_ant.prox

                # Guardar el dato y descartar el nodo
                dato = n_act.dato
                n_ant.prox = n_act.prox

        self.len -= 1
        return dato

    def remove(self, x):
        """Borra la primera aparición del valor x en la lista.
        Si x no está en la lista, levanta ValueError"""

        if self.len == 0:
            raise ValueError("Lista vacía")

        if self.prim.dato == x:
            # Caso particular: saltear la cabecera de la lista
            self.prim = self.prim.prox
        else:
            # Buscar el nodo anterior al que contiene a x (n_ant)
            n_ant = self.prim
            n_act = n_ant.prox
            while n_act is not None and n_act.dato != x:
                n_ant = n_act
                n_act = n_ant.prox

            if n_act == None:
                raise ValueError("El valor no está en la lista.")

            # Descartar el nodo
            n_ant.prox = n_act.prox

        self.len -= 1

    def insert(self, i, x):
        """Inserta el elemento x en la posición i.
        Si la posición es inválida, levanta IndexError"""

        if i < 0 or i > self.len:
            raise IndexError("Posición inválida")

        nuevo = _Nodo(x)

        if i == 0:
            # Caso particular: insertar al principio
            nuevo.prox = self.prim
            self.prim = nuevo
        else:
            # Buscar el nodo anterior a la posición deseada
            n_ant = self.prim
            for pos in range(1, i):
                n_ant = n_ant.prox

                # Intercalar el nuevo nodo
                nuevo.prox = n_ant.prox
                n_ant.prox = nuevo

        self.len += 1

    def show(self):
        nodo = self.prim
        while nodo:
            print(nodo.dato)
            nodo = nodo.prox

    def __len__(self):
        return self.len


class _Nodo:
    def __init__(self, dato, prox=None):
        self.dato = dato
        self.prox = prox
