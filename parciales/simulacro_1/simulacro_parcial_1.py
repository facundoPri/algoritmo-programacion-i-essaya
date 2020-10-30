def listar_multiplos(cantidad, numero):
    """
    Recibe dos numero enteros
    Devuelve una lista de determinada cantidad con los multiplos del segudo numero
    """
    lista = []
    for i in range(1, cantidad + 1):
        lista.append(numero * i)
    return lista


def main():
    while True:
        a = input("Cantidad: ")
        b = input("Numero: ")
        if not a.isdigit() or not b.isdigit():
            continue
        print(listar_multiplos(int(a), int(b)))
        break


main()


def subcadenas(lista_cadenas, n):
    """
    Recibe una lista de cadenas y un numero
    Devuelve una lista de cadenas donde la longitud maxima de sus cadenas en de n
    """
    nueva_lista = []
    nueva_cadena = ""
    cadena_unica = "".join(lista_cadenas)
    for i, letra in enumerate(cadena_unica, 1):
        nueva_cadena += letra
        if i % n == 0 or i == len(cadena_unica):
            nueva_lista.append(nueva_cadena)
            nueva_cadena = ""
    return nueva_lista


def sacudir_matriz(matriz):
    """
    Recibe una matriz,
    Mueve las filas impares a la izquierda y las pares a la derecha de esta misma matriz
    """
    for i, fila in enumerate(matriz):
        if i % 2 == 0:
            fila.insert(0, fila.pop())
        else:
            fila.append(fila.pop(0))
