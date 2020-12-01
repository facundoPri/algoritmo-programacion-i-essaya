import csv


def calcular_contacto(ruta_archivo, nombre_persona):
    """
    Reciba la ruta a un archivo con formato (<nombre persona>;<lugar>;<momento>) y el nombre de una persona
    Devuelva un conjunto con todas las personas con las que tuvo contacto.
    """
    with open(ruta_archivo) as f:
        archivo_localizaciones = csv.reader(f, delimiter=";")
        lugares_hora = {}
        contacto = set()
        for nombre, lugar, momento in archivo_localizaciones:
            lugares_hora[(lugar, momento)] = lugares_hora.get((lugar, momento), [])
            lugares_hora[(lugar, momento)].append(nombre)
        for personas in lugares_hora.values():
            if nombre_persona in personas:
                personas.remove(nombre_persona)
                contacto.update(personas)
        return contacto


# print(calcular_contacto("personas_lugar_hora.csv", "juan"))

gyms = {
    "gym1": (1, 1),
    "gym2": (2, 2),
    "gym3": (3, 3),
    "gym4": (4, 4),
    "gym5": (5, 5),
    "gym6": (6, 6),
    "gym7": (7, 7),
    "gym8": (8, 8),
    "gym9": (9, 9),
}


def calcular_dist(x1, y1, x2, y2):
    """
    Recibe dos coordenadas
    Devuelve la distancia entre ellas
    """
    return abs(x1 - x2) + abs(y1 - y2)


def calcular_gym_mas_cercano(ruta_archivo, gyms):
    """
    Recibe la ruta de un archivo con formato (<pokemon>;<tipo>;<pos_x>,<pos_y>) y un diccionarion con gimnasios y su posicion
    Crea un nuevo archivo con formato (<pokemon;<tipo>;<gimnasio más cercano>)
    """
    with open(ruta_archivo) as f_pokemons, open("gyms_mas_cerca.csv", "w") as resultado:
        pokemons = csv.reader(f_pokemons, delimiter=";")
        gym_cercanos = csv.writer(resultado, delimiter=";")
        for pokemons, tipo, p_x, p_y in pokemons:
            mas_cerca = list(gyms.items())[0]

            for nombre, posicion in list(gyms.items())[1:]:
                print(nombre, posicion)


# print(calcular_gym_mas_cercano("pokemons.csv", gyms))


class App:
    def __init__(self, nombre, espacio):
        self.nombre = nombre
        self.espacio = espacio


class Smartphone:
    def __init__(self, modelo, memoria_total):
        self.modelo = modelo
        self.memoria = memoria_total
        self.apps_instaladas = []

    def __str__(self):
        apps = [f"/n{app}" for app in self.apps_instaladas]
        return f"{self.modelo}, espacio libre: {self.memoria}, apps instaladas: {apps}"

    def instalar(self, app):
        if app.espacio > self.memoria:
            raise Exception("El smartphone no cuenta con espacio suficiente")
        if app in self.apps_instaladas:
            raise Exception("La app ya esta instalada")
        self.apps_instaladas.append(app)
        self.memoria -= app.espacio

    def desinstalar(self, app):
        if not app in self.apps_instaladas:
            raise Exception("El smartphone no tiene esa app instalada")
        self.apps_instaladas.remove(app)
        self.memoria += app.espacio
