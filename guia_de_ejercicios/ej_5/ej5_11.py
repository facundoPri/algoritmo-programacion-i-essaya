def buscar_digito_numero(digito, numero):
    '''
    Recibe un digito y un numero 
    Devuelve si exite el digito en el numero dado
    '''
    existe = False
    for i in str(numero):
        if i == str(digito):
            existe = True
    return existe


print(buscar_digito_numero(2, 1010))
