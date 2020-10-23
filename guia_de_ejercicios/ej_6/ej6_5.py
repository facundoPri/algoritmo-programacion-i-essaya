def devolver_iniciales(cadena):
    """
    Recibe una cadena de caracteres
    Devuelve las iniciales
    """
    resultado = cadena[0]
    for i in range(1, len(cadena)):
        if cadena[i] == " ":
            resultado += cadena[i + 1]
    return resultado


def devolver_primera_mayuscula(cadena):
    """
    Recibe una cadena de caracteres
    Devuelve la cadena pero con las primeras letras de cada palabra en mayuscula
    """
    resultado = cadena[0].upper()
    for i in range(0, len(cadena) - 1):
        if cadena[i] == " ":
            resultado += cadena[i + 1].upper()
        else:
            resultado += cadena[i + 1]
    return resultado


def devolver_palabras_empiezan_a(cadena):
    """
    Recibe una cadena de caracteres
    Devuelve las palabas que arrancan con a
    """
    resultado = ""
    seleccionando = False
    letras_correctas = ("a", "A")
    for i in range(0, len(cadena)):
        if i == 0 and cadena[i] in letras_correctas:
            seleccionando = True
        if cadena[i] == " " and cadena[i + 1] in letras_correctas:
            seleccionando = True
        elif cadena[i] == " " and not cadena[i + 1] in letras_correctas:
            seleccionando = False
        if seleccionando:
            resultado += cadena[i]
    return resultado
