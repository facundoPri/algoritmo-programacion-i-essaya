def es_subcadena(cadena, subcadena):
    """
    Recibe dos cadena
    Devuelve si la segunda cadena esta contenida en la primera
    """
    return subcadena in cadena


def devolver_anterior_alfabeto(cadena1, cadena2):
    """
    Recibe dos cadenas
    Devuelve la que venga antes en el orden alfabetico
    """
    if cadena1 < cadena2:
        return cadena1
    else:
        return cadena2
