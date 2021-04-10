# La suma digital de un número n es la suma de sus dígitos. Escribir la función recursiva suma_digital(n) que recibe un número entero positivo y devuelve su suma digital.
# No se permite convertir el número a cadena.
# Ejemplo: suma_digital(2019) → 12 (porque 2+0+1+9 = 12).


def suma_digital(n, total=0):
    if n // 10 == 0:
        total += n
        return total
    total += n - (n // 10) * 10
    return suma_digital(n // 10, total)


print(suma_digital(2019092))
