def convertir_f_c(grados_f):
    '''
    Recibe grados fahrenheit y los convierte a grados celsius
    '''
    grados_c = (grados_f - 32) * 5/9
    return grados_c


print(convertir_f_c(41))
