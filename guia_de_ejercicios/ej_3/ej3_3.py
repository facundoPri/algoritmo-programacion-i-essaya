def calcular_producto_maximo(numero1, numero2, numero3, numero4):
    mayor_producto = 0
    for n in [numero1, numero2, numero3, numero4]:
        for x in [numero1, numero2, numero3, numero4]:
            producto = (n * (x * (n != x)))
            mayor_producto = max(mayor_producto, producto)

    return mayor_producto


assert calcular_producto_maximo(1, 5, -2, -4) == 8
assert calcular_producto_maximo(1, 5, -2, -10) == 20
assert calcular_producto_maximo(0, 10, -2, -10) == 20
