# Implementar la función merge en forma recursiva.
# La función recibe dos listas ordenadas y devuelve una lista con los elementos intercalados ordenadamente.


def merge(lista1, lista2, final=[], index=0):
    lista1_cond = index > len(lista1) - 1
    lista2_cond = index > len(lista2) - 1

    if lista1_cond and lista2_cond:
        return final

    if not lista1_cond:
        valor1 = lista1[index]
        final.append(valor1)

    if not lista2_cond:
        valor2 = lista2[index]
        final.append(valor2)

    return merge(lista1, lista2, final, index + 1)


lista1 = [1, 3, 5, 7, 9]
lista2 = [2, 4, 6, 8]
print(merge(lista1, lista2))
