def numeros_triangulares():
    cantidad = int(input('Ingresar un numero: '))
    for i in range(1, cantidad + 1):
        resultado = i*(i+1)/2
        print(i, ' - ', resultado)


numeros_triangulares()
