def sumar_matrices(m1, m2):
    """
    Suma dos matrices de igual dimension.
    Devuelve una matriz.
    """
    resultado = []
    for fila in range(len(m1)):
        resultado.append([])
        for columna in range(len(m1[fila])):
            suma = m1[fila][columna] + m2[fila][columna]
            resultado[fila].append(suma)
    return resultado


matriz1 = [[2, 2], [1, 1]]
matriz2 = [[1, 3], [4, 5]]
print(sumar_matrices(matriz1, matriz2))
