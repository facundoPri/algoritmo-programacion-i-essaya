def convertir_entero_romano(numero):
    """
    Recibe un numero entero y devuelve su equivalente en numeros romanos
    """
    mil = numero // 1000
    cien = numero % 1000 // 100
    diez = numero % 100 // 10
    uno = numero % 10 // 1

    numero_romano = ''
    if 1 <= mil <= 3:
        numero_romano += 'M' * mil

    if 1 <= cien <= 3:
        numero_romano += 'C' * cien
    elif cien == 4:
        numero_romano += 'CD'
    elif 5 <= cien <= 8:
        resto = cien % 5
        numero_romano += 'D'+'C'*resto
    elif cien == 9:
        numero_romano += 'CM'

    if 1 <= diez <= 3:
        numero_romano += 'X' * diez
    elif diez == 4:
        numero_romano += 'XL'
    elif 5 <= diez <= 8:
        resto = diez % 5
        numero_romano += 'L'+'X'*resto
    elif diez == 9:
        numero_romano += 'XC'

    if 1 <= uno <= 3:
        numero_romano += 'I' * uno
    elif uno == 4:
        numero_romano += 'IV'
    elif 5 <= uno <= 8:
        resto = uno % 5
        numero_romano += 'V'+'I'*resto
    elif uno == 9:
        numero_romano += 'IX'

    return numero_romano


def main():
    '''
    Llama un input pidiendo numeros y imprime en pantalla el equivalente a ese numero en romanos
    '''
    numero = int(input('Ingresar numero: '))
    numero_romano = convertir_entero_romano(numero)
    print(numero_romano)


main()
