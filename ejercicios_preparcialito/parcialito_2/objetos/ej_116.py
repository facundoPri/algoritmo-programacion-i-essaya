"""
Implementar la clase Caramelera, que recibe en su constructor la cantidad de caramelos que puede contener, y tiene el siguiente comportamiento:

>>> c = Caramelera(20)            >>> c.sacar_caramelos(50)
>>> c.poner_caramelos(10)        Traceback (most recent call last):
>>> c.sacar_caramelos(4)         ...
>>> c.caramelos()                ValueError: No quedan tantos caramelos!
6                                >>> c.poner_caramelos(50)
>>> print(c)                     Traceback (most recent call last):
Caramelera con 6/20 caramelos    ...
                                    ValueError: No queda lugar para tantos caramelos
"""


class Caramelera:
    def __init__(self, cantidad_max):
        self.cantidad_max = cantidad_max
        self.contiene = 0

    def poner_caramelos(self, cantidad):
        """Recibe una cantidad de caramelos y la suma a la cantidad que contiene la caramelera"""
        if cantidad > self.cantidad_max - self.contiene:
            raise ValueError("No queda lugar para tantos caramelo")
        self.contiene += cantidad

    def sacar_caramelos(self, cantidad):
        """Recibe una cantidad de caramelos y la resta a la cantidad que contiene la caramelera"""
        if cantidad > self.contiene:
            raise ValueError("No queda lugar para tantos caramelos")
        self.contiene -= cantidad

    def caramelos(self):
        """Devuelve la cantidad de caramelos que hay en la caramelera"""
        return self.contiene

    def __str__(self):
        return f"Caramelera con {self.contiene}/{self.cantidad_max} caramelos"
