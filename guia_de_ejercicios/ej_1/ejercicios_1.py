import math

# ej 1.1 - ej 1.2
print('ej 1.1 - ej 1.2')
print('')


def multipicacion(a, b):
    return a * b


print("multipicacion(3, 2)")
print(multipicacion(3, 2))

# ej 1.3
print('')
print('ej 1.3')
print('')

print('a-')


def perimetro(base, altura):
    return base * 2 + altura * 2


print("perimetro(2, 3)")
print(perimetro(2, 3))

print('')
print('b-')


def area(base, altura):
    return multipicacion(base, altura)


print("area(2, 3)")
print(area(2, 3))

print('')
print('c-')


def areaCordenadas(x1, x2, y1, y2):
    base = x2 - x1
    altura = y2 - y1
    return base * altura


print("areaCordenadas(1,4,2,4)")
print(areaCordenadas(1, 4, 2, 4))

print('')
print('d-')


def circuloPerimetro(radio):
    return 2 * math.pi * radio


print("circuloPerimetro(3)")
print(circuloPerimetro(3))

print('')
print('e-')


def circuloArea(radio):
    return math.pi * radio ** 2


print("circuloArea(3)")
print(circuloArea(3))

print('')
print('f-')


def esferaVolumen(radio):
    return 4 / 3 * math.pi * radio ** 3


print('esferaVolumen(3)')
print(esferaVolumen(3))

print('')
print('g-')


def trianguloHipotenusa(catetoOpuesto, catetoAdyacente):
    return math.sqrt(catetoOpuesto ** 2 + catetoAdyacente ** 2)


print('trianguloHipotenusa(5, 5)')
print(trianguloHipotenusa(5, 5))

# ej 1.4
print('')
print('ej 1.4')
print('')

print('a-')
for i in range(5):
    print(i * i)

print('')
print('b-')
for i in range(2, 6):
    print(i, 2 ** i)

# ej 1.5
print('')
print('ej 1.5')
print('')


def factorial(numero):
    resultado = 1
    for i in range(numero):
        resultado = resultado * (i + 1)
    return resultado


print(factorial(2))
print(factorial(5))

# ej 1.6
print('')
print('ej 1.6')
print('')

print('')
print('a-')


def sum_res_div_mult(numero_1, numero_2):
    suma = numero_1 + numero_2
    resta = numero_1 - numero_2
    divicion = numero_1 / numero_2
    multipicacion = numero_1 * numero_2
    print("Suma:", suma)
    print("Resta:", resta)
    print("Divicion:", divicion)
    print("Multiplicacion:", multipicacion)


sum_res_div_mult(10, 5)

print('')
print('b-')


def tabla_multiplicacion(numero):
    for i in range(10):
        print(i + 1, " * ", numero, " = ", (i + 1) * numero)


tabla_multiplicacion(2)

# ej 1.7
print('')
print('ej 1.7')
print('')


def repetir_1000(palabra):
    for i in range(1000):
        print(palabra, end=' ')


repetir_1000('hola')
