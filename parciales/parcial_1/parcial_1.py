from string import ascii_lowercase


def es_ipv4_valido(ipv4):
    '''
    Recibe una cadena de caracteres (ipv4)
    Devuelve si la cadena pasada esta en un formato valido
    '''
    numeros_separados = ipv4.split('.')
    if not len(numeros_separados) == 4:
        return False
    for numeros in numeros_separados:
        if not (numeros.isdigit() and 0 <= int(numeros) <= 255):
            return False
    return True


def main_pedir_ipv4():
    '''
    Funcion main del programa pedir direccion ipv4
    Le pide al usuario una direccion ipv4 valida y la imprime en pantalla
    '''
    ipv4 = input('Ingrese una direccion IPv4: ')
    while not es_ipv4_valido(ipv4):
        ipv4 = input('IPv4 Invalido - Ingrese nuevamente: ')
    print(ipv4)


def encriptografar_rotN(cadena, n):
    '''
    Recibe una cadena y un entero
    Devuele la encriptacion de la cadena en formato rotN
    '''
    nueva_cadena = ''
    for letra in cadena:
        index_letra = ascii_lowercase.index(letra)
        nuevo_index = (index_letra + n) % len(ascii_lowercase)
        nueva_cadena += ascii_lowercase[nuevo_index]
    return nueva_cadena


def diferencia_listas(primer_lista, segunda_lista):
    '''
    Recibe dos listas donde cada una no presenta elementos repetidos
    Devuelve un una nueva lista todos los elementos de la primera que no estan en la segunda
    '''
    nueva_lista = []
    for elemento in primer_lista:
        if not elemento in segunda_lista:
            nueva_lista.append(elemento)
    return nueva_lista
