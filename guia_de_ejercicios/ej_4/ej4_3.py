def imprimir_matiz_identidad(n):
    if n <= 0:
        return print('No puedo imprimir la matriz identidad correspondiente a la dimension', n)
    for i in range(n):
        print('0'*(i), '1', '0'*(n-(i+1)), sep='')


imprimir_matiz_identidad(100)
