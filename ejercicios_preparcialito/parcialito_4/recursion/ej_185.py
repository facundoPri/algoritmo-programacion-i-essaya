# El algoritmo de Euclides se utiliza para calcular el máximo común divisor entre
# dos números. El mismo consiste en lo siguiente:
# • Dados dos números enteros, $a$ y $b$, se divide el número mayor ($a$) por el
#   menor ($b$) y se obtiene el resto de la división entera ($r$).
# • En caso de que el resto ($r$) de la división sea cero, el divisor ($b$) es el m.c.d.
# • En otro caso, se vuelve al primer paso, dividiendo al divisor ($b$) por el resto ($r$).
# Escribir en Python una función recursiva que devuelva el máximo común divisor de un número mediante el algoritmo de Euclides.


def algoritmo_euclides(a, b):
    """Recibe dos numeros entero, se divide a por b, si el resto es 0 se devuelve b, caso contrario se llama la misma funcion pasando b y el resto """
    r = a % b
    if r == 0:
        return b
    else:
        return algoritmo_euclides(b, r)


print(algoritmo_euclides(30, 24))
