import gamelib

GRILLA_PX = 300
TEXTO_PX = 60
FILAS_CANTIDAD = 10


def juego_crear():
    """Inicializar el estado del juego"""
    grilla = [[""] * FILAS_CANTIDAD for i in range(FILAS_CANTIDAD)]
    return grilla


def averiguar_turno(juego):
    """
    Recibe el estado del juego
    Me devuelve la de quien es el turno, O o X
    """
    cantidad_o = 0
    cantidad_x = 0
    for fila in juego:
        for valor in fila:
            if not valor:
                continue
            if valor == "O":
                cantidad_o += 1
            elif valor == "X":
                cantidad_x += 1
    return "X" if cantidad_o > cantidad_x else "O"


def tranformar_pixeles_posicion(px_x, px_y):
    """
    Recibe las posiciones x e y en pixeles
    Devuelve la pasicion en la grilla matriz de x e y
    """
    pasos = GRILLA_PX // FILAS_CANTIDAD
    return px_x // pasos, px_y // pasos


def juego_actualizar(juego, px_x, px_y):
    """Actualizar el estado del juego

    px_x e px_y son las coordenadas (en pixels) donde el usuario hizo click.
    Esta función determina si esas coordenadas corresponden a una celda
    del tablero; en ese caso determina el nuevo estado del juego y lo
    devuelve.
    """
    estado_juego = juego
    if not (0 <= px_x <= GRILLA_PX and 0 <= px_y <= GRILLA_PX):
        return estado_juego
    turno = averiguar_turno(juego)
    x, y = tranformar_pixeles_posicion(px_x, px_y)
    if not estado_juego[y][x]:
        estado_juego[y][x] = turno
    return estado_juego


def crear_tablero():
    """
    Dibuja el tablero del juego
    """
    filas_px = GRILLA_PX // FILAS_CANTIDAD
    for fila in range(0, GRILLA_PX + 1, filas_px):
        gamelib.draw_line(fila, 0, fila, GRILLA_PX, fill="white", width=1)
        gamelib.draw_line(0, fila, GRILLA_PX, fila, fill="white", width=1)


def tranformar_posicion_pixeles(x, y):
    """
    Recibe las posiciones x e y en la grilla matriz
    Devuele las posiciones x e y en pixeles
    """
    pasos = GRILLA_PX // FILAS_CANTIDAD
    mitad = pasos // 2
    return x * pasos + mitad, y * pasos + mitad


def posicionar_piezas(juego):
    """
    Recibe el estado del juego
    Posiciona las piezas en sus respectivos pixeles
    """
    for y, fila in enumerate(juego):
        for x, valor in enumerate(fila):
            if valor:
                px_x, px_y = tranformar_posicion_pixeles(x, y)
                gamelib.draw_text(valor, px_x, px_y, size=15)


def juego_mostrar(juego):
    """Actualizar la ventana"""
    crear_tablero()
    posicionar_piezas(juego)
    turno = averiguar_turno(juego)
    gamelib.draw_text(
        f"Turno: {turno}", GRILLA_PX / 2, GRILLA_PX + (TEXTO_PX / 2), size=15
    )


def main():
    juego = juego_crear()

    # Ajustar el tamaño de la ventana
    gamelib.resize(GRILLA_PX, GRILLA_PX + TEXTO_PX)

    # Mientras la ventana esté abierta:
    while gamelib.is_alive():
        # Todas las instrucciones que dibujen algo en la pantalla deben ir
        # entre `draw_begin()` y `draw_end()`:
        gamelib.draw_begin()
        juego_mostrar(juego)
        gamelib.draw_end()

        # Terminamos de dibujar la ventana, ahora procesamos los eventos (si el
        # usuario presionó una tecla o un botón del mouse, etc).

        # Esperamos hasta que ocurra un evento
        ev = gamelib.wait()

        if not ev:
            # El usuario cerró la ventana.
            break

        if ev.type == gamelib.EventType.KeyPress and ev.key == "Escape":
            # El usuario presionó la tecla Escape, cerrar la aplicación.
            break

        if ev.type == gamelib.EventType.ButtonPress:
            # El usuario presionó un botón del mouse
            x, y = ev.x, ev.y  # averiguamos la posición donde se hizo click
            juego = juego_actualizar(juego, x, y)


gamelib.init(main)
