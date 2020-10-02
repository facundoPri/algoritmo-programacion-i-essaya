def convertir_f_a_c(grado_f):
    '''
    Recibe por parametro un valor en grados fahrenheit y lo convierte a grados
    '''
    grado_celsius = (grado_f - 32) * 5/9
    return grado_celsius


print(convertir_f_a_c(41))
