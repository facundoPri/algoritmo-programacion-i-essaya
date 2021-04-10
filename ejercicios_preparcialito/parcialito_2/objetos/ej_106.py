"""
Escribir la clase Polinomio, utilizando una lista para guardar los coeficientes
del mismo. Debe permitir las siguientes operaciones:

>>> p1 = Polinomio([2, 0, -1, 3])     >>> p1 == Polinomio([2, 0, -1, 3])
>>> print(p1)                         True
"2x^3 - x + 3"                        >>> p1 + p2
>>> p2 = Polinomio([1, 3])            ValueError("No tienen el mismo grado")
>>> print(p2)                         >>> p3 = p1 + Polinomio([0,1,1,-5])
"x + 3"                               >>> print(p3)
>>> p1 == p2                          "2x^3 + x^2 - 2"
False

Nota: no es necesario que el resultado de str() sea exactamente como en el
ejemplo. Es válido también una representación como 2x^3 - 1x^1 + 3x^0
"""


class Polinomio:
    def __init__(self, coeficientes):
        self.coeficientes = coeficientes

    def __str__(self):
        resultado = ""
        for i, numero in enumerate(self.coeficientes, start=1):
            if numero == 0:
                continue
            exponente = len(self.coeficientes) - i
            espacio = "" if resultado == "" else " "
            signo = f"{espacio}- " if numero < 0 else f"{espacio}+ "
            resultado += "" if signo == "+ " else signo
            coeficiente = "" if abs(numero) == 1 else abs(numero)
            exp = f"^{exponente}" if exponente > 1 else ""
            variable = "x" if exponente > 0 else ""
            resultado += f"{coeficiente}{variable}{exp}"
        return resultado

    def __eq__(self, otro):
        return self.coeficientes == otro.coeficientes

    def __add__(self, otro):
        if not len(self.coeficientes) == len(otro.coeficientes):
            raise ValueError("No tienen el mismo grado")
        resultado = [x + y for x, y in zip(self.coeficientes, otro.coeficientes)]
        return Polinomio(resultado)

    def __repr__(self):
        return f"Polinomio({self.coeficientes})"
