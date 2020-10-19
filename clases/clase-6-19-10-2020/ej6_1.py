def imprimir_dos_primeros_caracteres(cadena):
    print(cadena[:-2])


def imprimir_ultimos_tres(cadena):
    print(cadena[-3:])


def imprimir_inverso(cadena):
    print(cadena[::-1])


def imprimir_espejo(cadena):
    # print(cadena, '|', cadena[::-1], sep='')
    print(cadena + cadena[::-1])


def imprimir_cada_dos(cadena):
    print(cadena[::2])
