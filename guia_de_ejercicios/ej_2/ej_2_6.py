def imprimir_valores_pares_entre(numero_a, numero_b):
    '''
    Recibe dos numeros y imprime todos los valores pares entre es
    '''
    for i in range(numero_a + numero_a % 2, numero_b + 1, 2):
        print(i)


imprimir_valores_pares_entre(3, 15)
