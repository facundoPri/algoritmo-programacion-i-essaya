def es_par(n):
    return n % 2 == 0


def es_primo(n):
    if n < 1:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    return True
