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
    return 4/3 * math.pi * radio ** 3


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
