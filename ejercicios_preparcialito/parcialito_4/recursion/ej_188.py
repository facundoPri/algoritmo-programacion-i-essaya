# Implementar el algoritmo de búsqueda binaria de manera recursiva.


def busqueda_binaria_recursiva(numero, lista, base, tope):
    mitad = (base + tope) // 2
    numero_mitad = lista[mitad]
    print(
        f"numero: {numero}, base: {base},mitad: {mitad}, tope: {tope}, numero_mid: {numero_mitad}"
    )
    if base > tope:
        return False
    if numero == numero_mitad:
        # return mitad
        return True
    if numero > numero_mitad:
        return busqueda_binaria_recursiva(numero, lista, mitad + 1, tope)
    if numero < numero_mitad:
        return busqueda_binaria_recursiva(numero, lista, base, mitad - 1)


lista = [1, 3, 5, 7, 9, 10, 22, 56, 75, 93, 101]
print(busqueda_binaria_recursiva(56, lista, 0, len(lista)))
