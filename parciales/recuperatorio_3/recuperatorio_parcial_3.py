# Ej - 1
def dividir_pila(pila, n):
    """Recibe un pila y devuelve una lista de pilas con n elementos cada una hasta que la pila orignial este vacia"""
    resultado = []
    while not pila.esta_vacia():
        pila_invertir = Pila()
        for veces in range(n):
            if not pila.esta_vacia():
                pila_invertir.apilar((pila.desapilar()))
        nueva_pila = Pila()
        for veces in range(n):
            if not pila_invertir.esta_vacia():
                nueva_pila.apilar((pila_invertir.desapilar()))
        resultado.append(nueva_pila)
    return resultado


# Ej - 2
def merge(self, otra_lista):
    """Recibe otra lista enlazada y devuelve una nueva lista enlazada donde se encuentran las dos ordenadas"""
    ultimo_nodo = self.prim
    otro_ultimo_nodo = otra_lista.prim
    resultado = ListaEnlazada()
    while not ultimo_nodo == None and not otro_ultimo_nodo == None:
        if ultimo_nodo.dato < otro_ultimo_nodo.dato:
            resultado.append(ultimo_nodo.dato)
            ultimo_nodo = ultimo_nodo.prox
        else:
            resultado.append(otro_ultimo_nodo.dato)
            otro_ultimo_nodo = otro_ultimo_nodo.prox

    while not ultimo_nodo == None:
        resultado.append(ultimo_nodo.dato)
        ultimo_nodo = ultimo_nodo.prox
    while not otro_ultimo_nodo == None:
        resultado.append(otro_ultimo_nodo.dato)
        otro_ultimo_nodo = otro_ultimo_nodo.prox

    return resultado


# Ej - 3
def eliminar_elemento(cola, elemento):
    """Recibe un cola y un elemento, modifica la cola eliminando todos los elementos igual a elemento"""
    para_encolar = []
    while not cola.esta_vacia():
        valor = cola.desencolar()
        if not valor == elemento:
            para_encolar.append(valor)
    for valor in para_encolar:
        cola.encolar(valor)
