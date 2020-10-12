def encontrar_maximo_minimo_polinomio_2d(a, b, c):
    """
    Recibe com parametros los coeficientes a, b, c de un polimonio de segundo grado
    Devuelve su maximo o minimo
    """
    if a == 0:
        return 'Esto es una funcion lienal'
    max_min = ''
    if a > 0:
        max_min = 'Minima'
    else:
        max_min = 'Maxima'

    vertice_x = -b/2*a
    vertice_y = (4*a*c-b**2)/4*a
    return max_min, vertice_x, vertice_y


def encontrar_raices_polinomio_2d(a, b, c):
    """
    Recibe los coeficientes de un polinomio de segundo grado
    """
    if a == 0:
        return 'Esto es una funcion lienal'
    if b**2 < 4*a*c:
        return 'Raiz negativa alert'
    raiz_1 = (-b+(b**2-4*a*c)**0.5)/2*a
    raiz_2 = (-b-(b**2-4*a*c)**0.5)/2*a
    return raiz_1, raiz_2


def calcular_interseccion_2_rectas(pendiente1, ordenada1, pendiente2, ordenada2):
    """
    Recibe la pendiente y ordenara de origen de dos rectas
    Devulve las cordenadas de la interseccion
    """
    if pendiente1 == pendiente2:
        return 'Rectas son paralelas'
    x = (ordenada2-ordenada1)/(pendiente1 - pendiente2)
    y = pendiente1 * x + ordenada1
    return x, y
