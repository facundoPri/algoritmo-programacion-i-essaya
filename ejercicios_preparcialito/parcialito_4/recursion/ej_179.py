# Realizar una función recursiva que reciba una lista de Python de números y devuelva una nueva lista eliminando los dígitos que son sucedidos por un número primo, devolviendo una lista igual a la recibida por parámetro pero sin los dígitos que cumplan la condición especificada. Nota: la función es_primo() ya se encuentra implementada.
# Ejemplo: eliminar_sucedidos_primo([4,7,6,11,13]) → [7,13]


def es_primo(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def eliminar_sucedidos_primo(lista, nueva_lista=[]):
    print(f"lista: {lista}, nueva_lista: {nueva_lista}")
    if len(lista) == 0:
        return nueva_lista
    if es_primo(lista[0]):
        nueva_lista.pop()
    nueva_lista.append(lista[0])

    return eliminar_sucedidos_primo(lista[1:], nueva_lista)


print(eliminar_sucedidos_primo([4, 7, 6, 11, 12, 13]))
