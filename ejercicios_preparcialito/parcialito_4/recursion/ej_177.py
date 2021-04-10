# Alan, Bárbara y Grace juegan al ping-pong. El que gana un partido sigue jugando,
# mientras que el que lo pierde es reemplazado por el que no jugaba.
# El primer partido es entre Romeo y Dante. Se gana una cerveza el primero
# que gana tres partidos seguidos. Implementar una función
# recursiva  que simule este juego y devuelva quien ganó. Suponer que la
# probabilidad de ganar un partido es igual para ambos.
# Nota: para simular el resultado de cada parido en forma aleaoria,
# utilizar la función random.choice.

from random import choice

jugadores = ["Alan", "Barbara", "Grace"]


def partida(jugador1, jugador2, ex_ganador, ganados):
    """Mejor de 3"""
    ganador = choice([jugador1, jugador2])
    print(f"Ganador: {ganador}, Victorias: {ganados+1}")
    if ex_ganador == ganador:
        ganados += 1
        if ganados == 3:
            return ganador
        else:
            return partida(jugador1, jugador2, ganador, ganados)
    else:
        return partida(jugador1, jugador2, ganador, 1)


# print(partida("Romeo", "Dante", "", 0))


def jugar(jugador1, jugador2, aciento):
    print(f"{jugador1} vs {jugador2}")
    ganador = partida(jugador1, jugador2, "", 0)
    print(f"Ganador: {ganador}")
    if not len(aciento) == 0:
        proximo = aciento.pop()
        return jugar(ganador, proximo, aciento)
    else:
        return ganador


print(f"Ganador final: {jugar('Romeo', 'Dante', jugadores)}")
