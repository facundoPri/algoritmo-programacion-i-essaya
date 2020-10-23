def pedir_entero(mensaje, max, min):
    """
    Recibe un mensaje, un numero maximo y un numero minimo
    Le pide al usuario para que esciba un numero entre el max y el min y lo devuelve si es valido
    """
    numero = input(f"{mensaje} [{min}...{max}]: ")
    while not (not numero.isalpha() and min <= int(numero) <= max):
        print(f"Por favor ingresar un número entre {min} y {max}")
        numero = input(f"{mensaje} [{min}...{max}]: ")
    print(numero)


pedir_entero("Cual es tu numero favorito?", 50, -50)
