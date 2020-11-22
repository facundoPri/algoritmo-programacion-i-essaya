"""
Se tiene un diccionario donde cada clave es el título de una canción (cadena), y cada valor la duración de la canción (en segundos).

Se tiene asimismo otro diccionario donde cada clave es el título de una lista de reproducción (cadena), y cada valor una lista con títulos de canción que la componen.

Se pide implementar una función que reciba como parámetros ambos diccionarios, y devuelva en forma de diccionario las duraciones de cada lista de reproducción. (El diccionario devuelto debe tener como claves los títulos de lista, y como valor la duración en segundos.)
"""

canciones = {"test1": 60, "test2": 120, "test3": 40, "test4": 600}
playlist = {
    "verano": ["test1", "test2", "test2"],
    "verano": ["test1", "test2", "test2"],
    "gym": ["test4", "test2", "test1"],
}


def calcular_duracion_playlists(canciones, playlist):
    """
    Recibe dos diccionarios, uno con las canciones y su duracion, otro con playlist y sus canciones
    Devuelve un diccionario con la duracion de cada playlist
    """
    duracion_playlists = {}
    for nombre, musicas in playlist.items():
        duracion_playlists[nombre] = 0
        for musica in musicas:
            if musica in canciones:
                duracion_playlists[nombre] += canciones[musica]
    return duracion_playlists


print(calcular_duracion_playlists(canciones, playlist))
