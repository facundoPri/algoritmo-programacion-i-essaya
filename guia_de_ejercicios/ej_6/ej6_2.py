def separar_caracteres(cadena, separador):
    """
    Recibe una cadena de caracteres y un caracter separador
    Devuelve la cadena de caracteres pero entre cada caracter aparece el separador
    """
    resultado = ""
    for letra in cadena:
        resultado += letra
        resultado += separador
    return resultado[:-1]


def remplazar_espacios(cadena, separador):
    """
    Recibe una cadena y un separador
    Devuelve la cadena pero remplazando los espacios por un separador
    """
    resultado = ""
    for caracter in cadena:
        if caracter == " ":
            resultado += separador
        else:
            resultado += caracter
    return resultado


def reemplazar_digitos_caracter(cadena, reemplazo):
    """
    Recibe una cadena y un remplazo
    Devuelve la cadena pero reemplazando los posibles digitos
    """
    resultado = ""
    for letra in cadena:
        if letra.isdigit():
            resultado += reemplazo
        else:
            resultado += letra
    return resultado


def insertar_caracter_cada_tres(cadena, caracter):
    """
    Recibe una cadena y un caracter
    Devuelve la cadena agregando cada 3 en nuevo caracter
    """
    resultado = cadena[:3]
    for i in range(3, len(cadena), 3):
        resultado += caracter
        resultado += cadena[i : 3 + i]
    return resultado
