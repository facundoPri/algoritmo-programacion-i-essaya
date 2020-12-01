"""
Se pide implementar la clase TwitterUser con los siguientes métodos:

__init__(): recibe como parámetro el nombre del usuario.
tweet(): recibe como parámetro un mensaje (se debe validar que no sobrepase los 280 caracteres) y lo agrega —con la fecha actual— a la lista de tuits del usuario. (Para obtener la fecha actual, se puede importar el módulo datetime, e invocar datetime.datetime.now())
follow(): recibe como parámetro otro usuario (de tipo TwitterUser) y lo guarda como un usuario al que se está siguiendo.
get_timeline(): devuelve una lista con los mensajes que tuitearon los usuarios a los que se está siguiendo. Debe ser una lista de tuplas tal que: (fecha, nombre_usuario, mensaje). Este método no toma parámetros, y la lista devuelta debe estar ordenada por fecha.
"""
from datetime import datetime


class TwitterUser:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tuits = []
        self.siguiendo = []

    def tweet(self, mensaje):
        if len(mensaje) > 280:
            raise ValueError("Mensaje invalido")
        self.tuits.append({"mensaje": mensaje, "fecha": datetime.now()})

    def follow(self, usuario):
        self.siguiendo.append(usuario)

    def get_timeline(self):
        timeline = []
        for usuario in self.siguiendo:
            for tuit in usuario.tuits:
                timeline.append((tuit["fecha"], usuario.nombre, tuit["mensaje"]))
        return sorted(timeline, key=lambda x: x[0])


usuario1 = TwitterUser("facu")
usuario2 = TwitterUser("juan")
usuario3 = TwitterUser("fran")
usuario1.tweet("Hola como estas")
usuario2.tweet("Soy Juan")
usuario1.tweet("Soy Facu")
usuario3.follow(usuario1)
usuario3.follow(usuario2)
usuario3.get_timeline()
