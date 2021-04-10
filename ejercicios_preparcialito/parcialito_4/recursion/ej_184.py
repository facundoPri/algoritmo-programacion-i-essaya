# Sea la siguiente operación, aplicable a cualquier número entero positivo:
# • Si el número es par, se divide por 2.
# • Si el número es impar, se multiplica por 3 y se suma 1.
# La conjetura de Collatz dice que, para cualquier número con el que
# comencemos, si aplicamos la operación sucesivamente, siempre alcanzaremos el
# número 1. Escribir la función recursiva collatz(n) que imprime la secuencia de
# operaciones comenzando desde el número n, y terminando en el número 1. Ejemplo:
# collatz(5) → 5 16 8 4 2 1


def collatz(numero):
    print(numero)
    if numero == 1:
        return
    elif numero % 2 == 0:
        numero = numero / 2
        return collatz(numero)
    else:
        numero = (numero * 3) + 1
        return collatz(numero)


collatz(30)
