def calcular_suma_promedio():
    '''
    Recibe numeros mediante una sucesin de inputs
    Devuelve un contados, la suma y el promedio
    '''
    numero = 0
    contador = 0
    suma = 0
    while not numero == -1:
        suma += numero
        contador += 1
        numero = int(input('Ingrese un numero: '))
    return contador, suma, suma/contador


def main():
    print(calcular_suma_promedio())


main()
