from lista_enlazada import ListaEnlazada


def suma_acumulativa(lista):
    nueva_lista = ListaEnlazada()
    acumulacion = 0
    nodo_actual = lista.prim
    while nodo_actual:
        acumulacion += nodo_actual.dato
        nodo_actual = nodo_actual.prox
        nueva_lista.append(acumulacion)
    return nueva_lista


lista_e = ListaEnlazada()
lista_e.append(1)
lista_e.append(4)
lista_e.append(1)
lista_e.append(1)
lista_e.append(1)
lista_e.append(1)

nueva_lista = suma_acumulativa(lista_e)
nueva_lista.show()
