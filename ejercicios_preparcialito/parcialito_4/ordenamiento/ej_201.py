# Implementar el algoritmo de ordenamiento por selección utilizando el mínimo en vez del máximo.


def org_seleccion(lista):
    """Algoritmo de ordenamiento por seleccion utilizando el minino"""

    for index, numero in enumerate(lista):
        print(index, numero)
        p = buscar_menor(lista, index)
        lista[p], numero = numero, lista[p]
    return lista


def buscar_menor(lista, comienzo):
    """Recibe una lista y el indice donde comieza
    Devuelve la posicion del menor"""
    menor = lista[comienzo]
    menor_index = comienzo
    for index, numero in enumerate(lista[comienzo:]):
        if menor > numero:
            menor = numero
            menor_index = index
    return menor_index + comienzo


print(org_seleccion([1, 9, 2, 4, 5, 1, 23, 8]))
