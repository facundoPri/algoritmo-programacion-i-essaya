def eliminar_posiciones_pares(lista):
    elementos_en_posiciones_pares = []
    for i in range(len(lista)):
        if i % 2 == 0:
            elementos_en_posiciones_pares.append(lista[i])
    for elemento in elementos_en_posiciones_pares:
        lista.remove(elemento)


lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(eliminar_posiciones_pares(lista))
print(lista)
