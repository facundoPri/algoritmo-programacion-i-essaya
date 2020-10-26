def esta_ordenada(tupla):
    """
    Recibe una tubla y devuelve si esta ordenada o no
    """
    for i in range(0, len(tupla)):
        if not tupla[len(tupla) - 1] == tupla[i] and tupla[i] > tupla[i + 1]:
            return False
    return True
