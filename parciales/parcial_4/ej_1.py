"""
Ej_1 - Hacer una función recursiva que recibe una lista L y una función f, y devuelve una nueva lista que contiene al principio todos los elementos de L para los que f devuelve True, y al final el resto de los elementos. No es necesario mantener el orden relativo de los elementos en cada grupo. Ejemplo: particionar([7,8,3,5,2], es_par) → [8,2,5,3,7]
"""


def es_par(n):
    return n % 2 == 0


def particionar(lista, funcion, resultado=[]):
    if len(resultado) == len(lista):
        return resultado
    valor = lista[len(resultado)]
    if funcion(valor):
        return particionar(lista, funcion, [valor] + resultado)
    else:
        return particionar(lista, funcion, resultado + [valor])


lista = [7, 8, 3, 5, 2]
print(particionar(lista, es_par))
