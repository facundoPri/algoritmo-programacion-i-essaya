def separar_por_miles(cadena):
    """
    Recibe una cadena
    Devuelve la cadena separada por miles
    """
    cadena = cadena[::-1]
    resultado = cadena[:3]
    for i in range(3, len(cadena), 3):
        resultado += "."
        resultado += cadena[i : 3 + i]
    return resultado[::-1]


print(separar_por_miles("12345678"))
