# Realizar una función recursiva en Python que reciba un número entero y devuelva el producto de sus dígitos.
# Ejemplo: producto_digital(356) → 90, pues 3 . 5 . 6 = 90.


def producto_digital(n, producto=1):
    if n // 10 == 0:
        producto *= n
        return producto

    digito = n - ((n // 10) * 10)
    return producto_digital(n // 10, producto * digito)


print(producto_digital(322))
