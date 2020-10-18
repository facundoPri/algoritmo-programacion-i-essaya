from random import randrange


def mayor_menor_igual(numero, comparacion):
    """
    Recibe dos numero y devuelve si el segundo numero es igual, mayor o menor al primero
    """
    if numero == comparacion:
        return 'Adivinaste!'
    elif numero > comparacion:
        return 'Es menor'
    elif numero < comparacion:
        return 'Es mayor'


def main():
    comparacion = randrange(1, 100)
    numero = 0
    while numero != comparacion:
        numero = int(input('Ingrese un número: '))
        resultado = mayor_menor_igual(numero, comparacion)
        print(resultado)


main()
