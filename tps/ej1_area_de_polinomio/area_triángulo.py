from vectores import *


def calcular_area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    '''
    Recibe 3 puntos en R**3 y me devuelve el area del triangulo que se forma entre ellos
    '''
    A = (x1, y1, z1)
    B = (x2, y2, z2)
    C = (x3, y3, z3)
    AB = diferencia(*B, *A)
    AC = diferencia(*C, *A)
    producto_vectorial = calcular_producto_vectorial(*AB, *AC)
    return norma(*producto_vectorial)/2


assert calcular_area_triangulo(1, 0, 0, 3, 1, 0, 2, -1, 0) == 1.5
assert calcular_area_triangulo(1, 1, 3, 3, 1, 1, 2, -1, 1) == 3.0
assert calcular_area_triangulo(0, 0, 0, 1, 0, 0, 0, 0, 1) == 0.5
