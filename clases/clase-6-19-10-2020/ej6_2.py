def separar_cadena(cadena, separador):
    separada = ''
    for letra in cadena:
        separada += letra
        separada += separador
    return separada[:-1]


def reemplazar_espacios(cadena, caracter):
    reemplazada = ''
    for c in cadena:
        if c == ' ':
            reemplazada += caracter
        else:
            reemplazada += c
    return reemplazada


def insetar_cada_n(cadena, caracter, n):
    reemplazada = cadena[:n]
    for i in range(n, len(cadena), n):
        reemplazada += caracter
        reemplazada += cadena[i:i+n]
    return reemplazada


print(insetar_cada_n('1234506780', '.', 3))
