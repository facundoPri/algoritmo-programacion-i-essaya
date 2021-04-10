from cola import Cola


def buscar_en(cola, elemento):
    """
    Recibe una cola y un elemento
    Devuelve un booleando si el elemento esta o no en la cola
    """
    elemento_cola = cola._frente
    while True:
        if elemento == elemento_cola.dato:
            return True
        if elemento_cola.prox:
            elemento_cola = elemento_cola.prox
        else:
            return False


c = Cola()
c.encolar(1)
c.encolar(3)
c.encolar(8)
c.encolar(9)
c.encolar(0)
c.encolar(2)

buscar_en(c, 3)
