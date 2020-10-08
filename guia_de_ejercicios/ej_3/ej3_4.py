import math


def calcular_norma_vector(x, y, z):
    '''
    Recibe los tres parametros de un vector y devuelve la norma
    '''
    return math.sqrt(x**2 + y**2 + z**2)


print('a-')
print(calcular_norma_vector(3, 2, -4))


def calcular_vector_diferencia(x1, y1, z1, x2, y2, z2):
    '''
    Recibe dos vectores y devuelve el diferencial de ellos
    '''
    return x1-x2, y1-y2, z1-z2


print('')
print('b-')
print(calcular_vector_diferencia(8, 7, -3, 5, 3, 2))


def calcular_producto_vectorial(x1, y1, z1, x2, y2, z2):
    '''
    Recibe dos vectores y calcula el producto vectorial
    '''
    return (y1*z2 - z1*y2), (z1*x2 - x1*z2), (x1*y2 - y1*x2)


print('')
print('c-')
print(calcular_producto_vectorial(1, 4, -2, 3, -1, 0))


def calcular_area_triangulo(x1, y1, z1, x2, y2, z2, x3, y3, z3):
    '''
    Recibe 3 puntos en R**3 y me devuelve el area del triangulo que se forma entre ellos
    '''
    A = (x1, y1, z1)
    B = (x2, y2, z2)
    C = (x3, y3, z3)
    AB = calcular_vector_diferencia(*B, *A)
    AC = calcular_vector_diferencia(*C, *A)
    producto_vectorial = calcular_producto_vectorial(*AB, *AC)
    return calcular_norma_vector(*producto_vectorial)/2


print('')
print('d-')
print(calcular_area_triangulo(5, 8, -1, -2, 3, 4, -3, 3, 0))


def calcular_area_cuadrilatero_convexo(x1, y1, x2, y2, x3, y3, x4, y4):
    '''
    Recibe 4 puntos en R3 y me devuelve el area de un cuadrilatero convexo
    '''
    A = (x1, y1, 0)
    B = (x2, y2, 0)
    C = (x3, y3, 0)
    D = (x4, y4, 0)
    AC = calcular_vector_diferencia(*C, *A)
    BD = calcular_vector_diferencia(*D, *B)
    producto_vectorial = calcular_producto_vectorial(*AC, *BD)
    return calcular_norma_vector(*producto_vectorial)/2


print('')
print('e-')
print(calcular_area_cuadrilatero_convexo(4, 3, 5, 10, -2, 8, -3, -5))
