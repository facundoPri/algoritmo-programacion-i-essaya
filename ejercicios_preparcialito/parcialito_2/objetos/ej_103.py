"""
Suponiendo que se cuenta con la clase Vaca con el método sondear() que se comporta según el siguiente ejemplo:

>>> vaca = Vaca()
>>> vaca.sondear()
>>> "Muuuuu!"
Implementar la clase Ovni que cumpla el siguiente comportamiento:

>>> ovni = Ovni(“Stargazer”)                  >>> ovni.abducir(Vaca())
>>> print(ovni)                               EstacionDeSondeoOcupadaError
"Nave Stargazer (estación de sondeo vacía)"   >>> ovni.sondear()
>>> ovni.sondear()                            "Sondeando... ‘Muuuuu!’... Ups, el sujeto explotó"
EstacionDeSondeoVaciaError                    >>> print(ovni)
>>> ovni.abducir(Vaca())                      "Nave Stargazer (estación de sondeo vacía)"
>>> print(ovni)
"Nave Stargazer (estación de sondeo ocupada)"

Nota: Suponer que las excepciones EstacionDeSondeoVaciaError y EstacionDeSondeoOcupadaError ya existen.
"""


class Vaca:
    def sondear(self):
        return "Muuuuu!"


class Ovni:
    def __init__(self, nombre):
        self.nombre = nombre
        self.sujeto = None

    def __str__(self):
        estado = "ocupada" if self.sujeto else "vacia"
        return f"Nave {self.nombre} (estacion de sondeo {estado})"

    def abducir(self, sujeto):
        if self.sujeto:
            return print("EstacionDeSondeoOcupadaError")
        self.sujeto = sujeto

    def sondear(self):
        if not self.sujeto:
            return print("EstacionDeSondeoVaciaError")
        mensaje = f"Sondeando... ´{self.sujeto.sondear()}´... Ups, el sujeto explotó"
        self.sujeto = None
        return mensaje
