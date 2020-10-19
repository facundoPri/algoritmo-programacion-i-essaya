def es_primo(n):
    if n <= 0:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def armar_lista_primos(lista_numeros):
    primos = []
    for n in lista_numeros:
        if es_primo(n):
            primos += [n]
    return primos


def calcular_sumatoria_y_promedio(lista_numeros):
    sumatoria = 0
    for n in lista_numeros:
        sumatoria += n
    return sumatoria, sumatoria/len(lista_numeros)


def calcular_factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    return factorial


def listar_factoriales(lista_numeros):
    factoriales = []
    for n in lista_numeros:
        factoriales += [calcular_factorial(n)]
    return factoriales


print(listar_factoriales([1, 2, 3, 4, 5]))
