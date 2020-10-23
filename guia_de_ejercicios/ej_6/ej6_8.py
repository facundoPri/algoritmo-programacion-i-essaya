def convertir_binario_decimal(cadena):
    """
    Recibe una cadena de unos y zeros
    Devuelve el valor equivalente en decimales del binario
    """
    resultado = 0
    for i in range(0, len(cadena)):
        numero = int(cadena[i])
        resultado += numero * 2 ** i
    return resultado
