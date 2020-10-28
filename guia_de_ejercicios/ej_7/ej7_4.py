def calcular_producto_escalar(vector1, vector2):
    """
    Recibe dos vectores
    Devuelve el producto escalar entre los dos
    """
    producto_escalar = 0
    for index, valor in enumerate(vector1):
        producto_escalar += valor * vector2[index]
    return producto_escalar


def son_ortogonales(vector1, vector2):
    """
    Recibe dos vectores
    Devuelve si son ortogonales o no
    """
    return calcular_producto_escalar(vector1, vector2) == 0


def calcular_modulo_vector(vector):
    """
    Recibe un vector y devuelve su modulo
    """
    suma_cuadrados = 0
    for i in vector:
        suma_cuadrados += i ** 2
    return suma_cuadrados ** 0.5


def son_paralelas(vector1, vector2):
    """
    Recibe dos vectore
    Devuelve si son paralelas o no
    """
    multiplicacion_modulos = calcular_modulo_vector(vector1) * calcular_modulo_vector(
        vector2
    )
    return (
        abs(round(calcular_producto_escalar(vector1, vector2) / multiplicacion_modulos))
        == 1
    )
