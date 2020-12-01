"""
Se tiene una clase Ejercicio con los métodos calificar(n) y obtener_nota(), que reciben y devuelven, respectivamente, un número entero entre 0 y 10 (si no está calificado, obtener_nota debe levantar una excepción). Escribir una clase Examen que tenga los siguientes métodos:

un constructor que cree un Examen nuevo en base a una lista de Ejercicios
calificar(i,n), con i el número de ejercicio y n la calificación del mismo
esta_aprobado(), que devuelve si un Examen está aprobado o no. Un examen está aprobado si tiene el 60% de los ejercicios con nota mayor o igual a 6.
obtener_nota(), que devuelve la nota del Examen. Si esta aprobado, la misma es un promedio de la nota de todos los ejercicios. Sino, es un 2 independientemente del promedio.
"""


class Ejercicio:
    def __init__(self):
        self.nota = None

    def calificar(self, nota):
        if not 0 <= nota <= 10:
            raise ValueError("Nota invalida")
        self.nota = nota

    def obtener_nota(self):
        if not self.nota:
            raise ValueError("Noto inexistente")
        return self.nota


class Examen:
    def __init__(self, lista_ejercicios):
        self.ejercicios = lista_ejercicios

    def calificar(self, i, n):
        self.ejercicios[i].calificar(n)

    def esta_aprobado(self):
        cantidad_aprobados = 0
        for ejercicio in self.ejercicios:
            if ejercicio.obtener_nota() >= 6:
                cantidad_aprobados += 1
        return (cantidad_aprobados / len(self.ejercicios)) * 100 >= 60

    def obtener_nota(self):
        if not self.esta_aprobado():
            return 2
        suma_nota = 0
        for ejercicio in self.ejercicios:
            suma_nota += ejercicio.obtener_nota()
        return suma_nota / len(self.ejercicios)
