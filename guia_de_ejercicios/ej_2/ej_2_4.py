def convertir_f_c(grados_f):
    '''
    Recibe grados fahrenheit y los convierte a grados celsius
    '''
    grados_c = (grados_f - 32) * 5/9
    return grados_c


def tabla_converciones():
    for i in range(13):
        print((i)*10, ' ºF = ', convertir_f_c((i)*10), ' ºF')


tabla_converciones()
