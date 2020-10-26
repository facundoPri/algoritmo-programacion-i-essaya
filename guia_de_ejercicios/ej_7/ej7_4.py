def calcular_producto_escalar(vector1, vector2):
    """
    Recibe dos vectores
    Devuelve el producto escalar entre los dos
    """
    producto_escalar = vector1[0] * vector2[1] + vector1[1] * vector2[0]
    return producto_escalar


print(calcular_producto_escalar((3, 0), (5, 5)))
