def matriz(matriz1, matriz2):
    nueva_matriz = []
    for columna in list(zip(matriz1, matriz2)):
        nueva_matriz.append(list(columna))
    return nueva_matriz


matriz1 = [1, 2, 3, 4]
matriz2 = [5, 6, 7, 8]
print(matriz(matriz1, matriz2))
