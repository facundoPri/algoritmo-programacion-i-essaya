from cola import Cola


def cola_map(cola, f):
    nueva_cola = Cola()
    while not cola.esta_vacia():
        frente = cola.desencolar()
        nueva_cola.encolar(f(frente))
    return nueva_cola


c = Cola()
c.encolar(1)
c.encolar(2)
c.encolar(5)
c.encolar(3)
c.encolar(9)
c.encolar(4)

nueva_cola = cola_map(c, lambda x: x + 1)
while not nueva_cola.esta_vacia():
    print(nueva_cola.desencolar())
