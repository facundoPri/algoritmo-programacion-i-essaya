print('a-')


def par_impar(numero):
    '''
    Recibe un numero, si es par devuelve 0 si es impar 1
    '''
    return numero % 2


print(par_impar(10))
print(par_impar(5))

print('')
print('b-')


def impar_par(numero):
    '''
    Recibe un numero, si es par devuelve 1 si es impar 0
    '''
    return (numero // 2) % 2


print(impar_par(10))
print(impar_par(5))


print('')
print('c-')


def menor_unidad(numero):
    return numero % 10


print(menor_unidad(10))
print(menor_unidad(100))
print(menor_unidad(12))
print(menor_unidad(102))
print(menor_unidad(132))

print('')
print('d-')


def multiplo_diez(numero):
    return numero - menor_unidad(numero)


print(multiplo_diez(1002))
print(multiplo_diez(153))
