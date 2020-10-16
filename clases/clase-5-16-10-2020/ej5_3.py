from time import sleep


def verificar_contrania(contrasenia, intentos):
    '''
    '''
    for i in range(intentos):
        entrada = input('Ingrese la contrasenia: ')
        if entrada == contrasenia:
            return True
        sleep(i+1)
    return False


verificar_contrania("contrasenia", 5)
