class Nodo:
    def __init__(self, dato=None, prox=None):
        self.dato = dato
        self.prox = prox

    def __str__(self):
        return str(self.dato)


class ListaEnlazada:
    """Modela una lista enlazada."""

    def __init__(self):
        """Crea una lista enlazada vacía."""
        # referencia al primer nodo (None si la lista está vacía)
        self.prim = None
        # cantidad de elementos de la lista
        self.len = 0

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
        nuevo = Nodo(x)
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

    def append(self, valor):
        """Agrega un valor al ultimo puesto"""
        self.insert(self.len, valor)

    def merge(self, otra_lista):
        """Recibe otra lista enlazada y devuelve una nueva lista enlazada donde se encuentran las dos ordenadas"""
        ultimo_nodo = self.prim
        otro_ultimo_nodo = otra_lista.prim
        resultado = ListaEnlazada()
        while not ultimo_nodo == None and not otro_ultimo_nodo == None:
            if ultimo_nodo.dato < otro_ultimo_nodo.dato:
                # print(ultimo_nodo)
                resultado.append(ultimo_nodo.dato)
                ultimo_nodo = ultimo_nodo.prox
            else:
                # print(otro_ultimo_nodo)
                resultado.append(otro_ultimo_nodo.dato)
                otro_ultimo_nodo = otro_ultimo_nodo.prox

        while not ultimo_nodo == None:
            resultado.append(ultimo_nodo.dato)
            ultimo_nodo = ultimo_nodo.prox
        while not otro_ultimo_nodo == None:
            resultado.append(otro_ultimo_nodo.dato)
            otro_ultimo_nodo = otro_ultimo_nodo.prox

        return resultado


lista1 = ListaEnlazada()
lista1.append(3)
lista1.append(5)
lista1.append(9)
lista1.append(15)
lista2 = ListaEnlazada()
lista2.append(1)
lista2.append(2)
lista2.append(6)
lista2.append(10)
lista2.append(11)
lista2.append(13)
lista2.append(16)
lista2.append(26)

resultado = lista1.merge(lista2)

n_ant = resultado.prim
for pos in range(resultado.len):
    print(n_ant)
    n_ant = n_ant.prox
