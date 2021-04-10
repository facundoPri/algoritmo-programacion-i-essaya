# a. Dadas dos listas ordenadas de números, implementar una función que reciba estas dos listas y devuelva una nueva lista que tenga los elementos de ambas listas ordenados. El tiempo de ejecución de la función debe ser lineal (proporcional a la cantidad total de elementos de las dos listas).
# b. ¿En qué famoso algoritmo de ordenamiento se utiliza el algoritmo del punto anterior?

# a.
def merge(l1, l2):
    """Recibe dos listas y devuelve un unica lista ordenada"""
    i, j = 0, 0
    resultado = []
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            resultado.append(l1[i])
            i += 1
        else:
            resultado.append(l2[j])
            j += 1
    resultado += l1[i:]
    resultado += l2[j:]
    return resultado


l1 = [1, 3, 5, 7, 8, 10, 11, 14, 19]
l2 = [2, 3, 5, 6, 7, 8, 11, 19, 20, 25]

# b
"""
Esta funcion es la misma funcion merge usada en mergesort
"""
