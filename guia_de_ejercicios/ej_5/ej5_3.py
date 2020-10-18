from time import sleep


def verificar_contrasenia(contrasenia, intentos):
    """
    Le pregunta al usuario contrasenias hasta que se valide
    """
    contador_intentos = 0
    while contrasenia != input('Ingrese la contrasenia: '):
        contador_intentos += 1
        print('Contrasenia incorrecta (', intentos -
              contador_intentos, ' intento/s restante/s)', sep='')
        if contador_intentos >= intentos:
            print('Limite de intentos')
            return False
        sleep(contador_intentos)
    return True


def main():
    print(verificar_contrasenia('test', 3))


main()
