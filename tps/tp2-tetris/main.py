import gamelib
import tetris

ESPERA_DESCENDER = 8
RES = 400
RUTA_TECLAS_CONFIG = "teclas.txt"
RUTA_PIEZAS = "piezas.txt"
RUTA_PUNTUAJES = "puntuajes.txt"
RUTA_PARTIDA = "partida.txt"


def dibujar_grilla(juego):
    """
    Recibe el juego y dibuja el la grilla
    """
    ancho, alto = tetris.dimensiones(juego)
    proporcio = alto / ancho
    grilla_ancho = RES / proporcio
    columna_ancho = grilla_ancho / ancho
    panel_ancho = RES - grilla_ancho
    margen = RES / 10

    for columna in range(ancho):
        color = "#fff"
        if columna % 2 == 0:
            color = "#f4efe9"
        gamelib.draw_rectangle(
            (columna * columna_ancho),
            0,
            ((columna + 1) * columna_ancho),
            RES,
            fill=color,
            outline=color,
        )
    # Panel
    gamelib.draw_rectangle(
        grilla_ancho, 0, RES, RES, fill="#f4eee2", outline="#ecdbc4", width=2
    )
    # Texto
    gamelib.draw_text(
        "TETRIS", grilla_ancho + (panel_ancho / 2), margen, fill="#4f6dae", size=30
    )

def dibujar_pieza(juego):
    """
    Recibe el juego y dibuja la pieza actual
    """
    ancho, alto = tetris.dimensiones(juego)
    proporcio = alto / ancho
    grilla_ancho = RES / proporcio
    lado_bloque = grilla_ancho / ancho
    posiciones = tetris.pieza_actual(juego)
    for posicion in posiciones:
        x, y = posicion
        gamelib.draw_rectangle(
            x * lado_bloque,
            y * lado_bloque,
            (x + 1) * lado_bloque,
            (y + 1) * lado_bloque,
            fill="red",
        )


def dibujar_siguiente(juego, pieza):
    """
    Recibe el juego y la siguiente pieza
    Dibuja un panel para mostrarsela al usuario
    """
    ancho, alto = tetris.dimensiones(juego)
    proporcio = alto / ancho
    grilla_ancho = RES / proporcio
    lado_bloque = grilla_ancho / ancho
    panel_ancho = RES - grilla_ancho
    eje_y_pieza = list(zip(*pieza))[0]
    bloques_fila = max(eje_y_pieza) + 1
    centro_panel = grilla_ancho + panel_ancho / 2 - (bloques_fila * lado_bloque) / 2
    margen = RES * 2 / 10
    for posicion in pieza:
        x, y = posicion
        gamelib.draw_rectangle(
            (x * lado_bloque) + centro_panel,
            (y * lado_bloque) + margen,
            ((x + 1) * lado_bloque) + centro_panel,
            ((y + 1) * lado_bloque) + margen,
            fill="red",
        )


def dibujar_superficie(juego):
    """
    Recibe el juego y dibuja la superficie
    """
    ancho, alto = tetris.dimensiones(juego)
    proporcio = alto / ancho
    grilla_ancho = RES / proporcio
    lado_bloque = grilla_ancho / ancho
    for y in range(alto):
        for x in range(ancho):
            if tetris.hay_superficie(juego,x,y):
                gamelib.draw_rectangle(
                    x * lado_bloque,
                    y * lado_bloque,
                    (x + 1) * lado_bloque,
                    (y + 1) * lado_bloque,
                    fill="gray",
                )


def dibujar_game_over(tabla_record):
    """

    Dibuja la pantalla de game over cuando el juego termina
    """
    margen = RES / 10
    gamelib.draw_rectangle(0, 0, RES, RES, fill="#f4eee2", outline="#ecdbc4", width=2)
    gamelib.draw_text("GAME OVER", RES / 2, margen, fill="#4f6dae", size=30)
    for index, record in enumerate(tabla_record, start=1):
        nombre, puntos = record
        gamelib.draw_text(
            f"{index}- {nombre}: {puntos}",
            RES / 2,
            30 * index + margen + 20,
            fill="#4f6dae",
            size=20,
        )


def dibujar_puntuaje(juego, puntuaje):
    """
    Recibe el estado del juego y el puntuaje actual
    Dibuja en el panel los puntos
    """
    ancho, alto = tetris.dimensiones(juego)
    proporcio = alto / ancho
    grilla_ancho = RES / proporcio
    panel_ancho = RES - grilla_ancho
    margen = RES * 2 / 10
    gamelib.draw_text(
        f"Puntos: {int(puntuaje)}",
        grilla_ancho + (panel_ancho / 2),
        RES - margen,
        fill="#4f6dae",
        size=20,
    )


def main():
    # Inicializar el estado del juego
    gamelib.resize(RES, RES)
    teclas = tetris.cargar_teclas(RUTA_TECLAS_CONFIG)
    piezas = tetris.cargar_piezas(RUTA_PIEZAS)
    siguiente_pieza = tetris.generar_pieza(piezas)
    juego = tetris.crear_juego(tetris.generar_pieza(piezas))
    tabla_record = tetris.mostrar_tabla_records(RUTA_PUNTUAJES)
    juego_terminado = False
    puntuaje = 0
    salir = False

    timer_bajar = ESPERA_DESCENDER
    while gamelib.loop(fps=30) and not salir:
        gamelib.draw_begin()
        # Dibujar la pantalla
        dibujar_grilla(juego)
        dibujar_pieza(juego)
        dibujar_siguiente(juego, siguiente_pieza)
        dibujar_superficie(juego)
        dibujar_puntuaje(juego, puntuaje)
        if juego_terminado:
            dibujar_game_over(tabla_record)
            anotar = tetris.es_record(puntuaje, tabla_record)
            if anotar:
                nombre = gamelib.input("Ingresar nombre: ")
                tetris.guardar_puntuaje(RUTA_PUNTUAJES, nombre, int(puntuaje))
            dibujar_game_over(tabla_record)
            break
        gamelib.draw_end()

        for event in gamelib.get_events():
            if not event:
                break
            if event.type == gamelib.EventType.KeyPress:
                tecla = event.key
                # Actualizar el juego, según la tecla presionada
                if tecla in teclas:
                    if teclas[tecla] == "IZQUIERDA":
                        juego = tetris.mover(juego, -1)
                    elif teclas[tecla] == "DERECHA":
                        juego = tetris.mover(juego, 1)
                    elif teclas[tecla] == "DESCENDER":
                        timer_bajar = 1
                    elif teclas[tecla] == "SALIR":
                        salir = True
                    elif teclas[tecla] == "ROTAR":
                        juego = tetris.rotar(juego, piezas)
                    elif teclas[tecla] == "GUARDAR":
                        tetris.guardar_partida(
                            RUTA_PARTIDA, juego, puntuaje, siguiente_pieza
                        )
                    elif teclas[tecla] == "CARGAR":
                        partida = tetris.cargar_partida(RUTA_PARTIDA)
                        juego = partida["juego"]
                        siguiente_pieza = partida["siguiente_pieza"]
                        puntuaje = partida["puntuaje"]

        if not tetris.terminado(juego) and not juego_terminado:
            timer_bajar -= 1
            if timer_bajar == 0:
                timer_bajar = ESPERA_DESCENDER
                puntuaje += 0.3
                # Descender la pieza automáticamente
                juego, prox = tetris.avanzar(juego, siguiente_pieza)
                if prox:
                    siguiente_pieza = tetris.generar_pieza(piezas)
        else:
            juego_terminado = True


gamelib.init(main)
