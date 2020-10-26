def encajar_fichas(ficha1, ficha2):
    """
    Recibe dos fichas de domino
    Devuelve si las fichas encajan una con la otra
    """
    for i in ficha1:
        if i in ficha2:
            return True
    return False


def encajar_fichas_string(ficha1, ficha2):
    """
    Recibe dos fichas de domino adentro de una cadena de caracteres
    Devuelve si las fichas encajan una con la otra
    """
    ficha1 = ficha1.split("-")
    for i in ficha1:
        if i in ficha2:
            return True
    return False
