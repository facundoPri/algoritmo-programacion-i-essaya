def separar_caracteres(cadena, separador, cantidad):
    """
    Recibe una cadena de caracteres y un caracter separador
    Devuelve la cadena de caracteres pero entre cada caracter aparece el separador
    """
    resultado = ""
    inserciones = 0
    for letra in cadena:
        if inserciones == cantidad:
            return resultado + cadena[cantidad:]
        resultado += letra
        resultado += separador
        inserciones += 1
    return resultado[:-1]


def remplazar_espacios(cadena, separador, cantidad):
    """
    Recibe una cadena y un separador
    Devuelve la cadena pero remplazando los espacios por un separador
    """
    resultado = ""
    reemplazos = 0
    for indice in range(0, len(cadena)):
        if reemplazos == cantidad:
            return resultado + cadena[indice:]
        elif cadena[indice] == " ":
            resultado += separador
            reemplazos += 1
        else:
            resultado += cadena[indice]
    return resultado


def reemplazar_digitos_caracter(cadena, reemplazo, cantidad):
    """
    Recibe una cadena y un remplazo
    Devuelve la cadena pero reemplazando los posibles digitos
    """
    resultado = ""
    reemplazados = 0
    for i in range(0, len(cadena)):
        if reemplazados == cantidad:
            return resultado + cadena[i:]
        elif cadena[i].isdigit():
            resultado += reemplazo
            reemplazados += 1
        else:
            resultado += cadena[i]
    return resultado


def insertar_caracter_cada_tres(cadena, caracter, cantidad):
    """
    Recibe una cadena y un caracter
    Devuelve la cadena agregando cada 3 en nuevo caracter
    """
    resultado = cadena[:3]
    inserciones = 0
    for i in range(3, len(cadena), 3):
        if inserciones == cantidad:
            return resultado + cadena[i:]
        resultado += caracter
        resultado += cadena[i : 3 + i]
        inserciones += 1
    return resultado
