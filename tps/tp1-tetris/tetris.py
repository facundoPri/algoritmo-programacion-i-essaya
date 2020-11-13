from random import randint

ANCHO_JUEGO, ALTO_JUEGO = 9, 18
IZQUIERDA, DERECHA = -1, 1
CUBO = 0
Z = 1
S = 2
I = 3
L = 4
L_INV = 5
T = 6

PIEZAS = (
    ((0, 0), (1, 0), (0, 1), (1, 1)),  # Cubo
    ((0, 0), (1, 0), (1, 1), (2, 1)),  # Z (zig-zag)
    ((0, 0), (0, 1), (1, 1), (1, 2)),  # S (-Z)
    ((0, 0), (0, 1), (0, 2), (0, 3)),  # I (línea)
    ((0, 0), (0, 1), (0, 2), (1, 2)),  # L
    ((0, 0), (1, 0), (2, 0), (2, 1)),  # -L
    ((0, 0), (1, 0), (2, 0), (1, 1)),  # T
)


def generar_pieza(pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """
    if not pieza:
        pieza = randint(CUBO, T)
    return PIEZAS[pieza]


def trasladar_pieza(pieza, dx, dy):
    """
    Traslada la pieza de su posición actual a (posicion + (dx, dy)).

    La pieza está representada como una tupla de posiciones ocupadas,
    donde cada posición ocupada es una tupla (x, y).
    Por ejemplo para la pieza ( (0, 0), (0, 1), (0, 2), (0, 3) ) y
    el desplazamiento dx=2, dy=3 se devolverá la pieza
    ( (2, 3), (2, 4), (2, 5), (2, 6) ).
    """
    nuevas_posiciones = []
    for posicion in pieza:
        x, y = posicion
        if not (0 <= x <= ANCHO_JUEGO and 0 <= y <= ALTO_JUEGO):
            return pieza
        nueva_posicion = (x + dx, y + dy)
        nuevas_posiciones.append(nueva_posicion)
    return tuple(nuevas_posiciones)


def centrar_pieza(pieza):
    """
    Recibe una pieza (tupla de tupla)
    Devuelve la pieza centrada en el juego
    """
    pieza_centrada = trasladar_pieza(pieza, ANCHO_JUEGO // 2, 0)
    return pieza_centrada


def crear_juego(pieza_inicial):
    """
    Crea un nuevo juego de Tetris.

    El parámetro pieza_inicial es una pieza obtenida mediante
    pieza.generar_pieza. Ver documentación de esa función para más información.

    El juego creado debe cumplir con lo siguiente:
    - La grilla está vacía: hay_superficie da False para todas las ubicaciones
    - La pieza actual está arriba de todo, en el centro de la pantalla.
    - El juego no está terminado: terminado(juego) da False

    Que la pieza actual esté arriba de todo significa que la coordenada Y de
    sus posiciones superiores es 0 (cero).
    """
    juego = []
    pieza_centrada = centrar_pieza(pieza_inicial)
    for fila in range(ALTO_JUEGO):
        juego.append([])
        for columna in range(ANCHO_JUEGO):
            if (columna, fila) in pieza_centrada:
                juego[fila].append([False, True])
            else:
                juego[fila].append([False, False])
    return juego


def dimensiones(juego):
    """
    Devuelve las dimensiones de la grilla del juego como una tupla (ancho, alto).
    """
    return (len(juego[0]), len(juego))


def pieza_actual(juego):
    """
    Devuelve una tupla de tuplas (x, y) con todas las posiciones de la
    grilla ocupadas por la pieza actual.

    Se entiende por pieza actual a la pieza que está cayendo y todavía no
    fue consolidada con la superficie.

    La coordenada (0, 0) se refiere a la posición que está en la esquina
    superior izquierda de la grilla.
    """
    posicion = []
    for y, fila in enumerate(juego):
        for x, columna in enumerate(fila):
            if columna[1]:
                posicion.append((x, y))
    return tuple(posicion)


def hay_superficie(juego, x, y):
    """
    Devuelve True si la celda (x, y) está ocupada por la superficie consolidada.

    La coordenada (0, 0) se refiere a la posición que está en la esquina
    superior izquierda de la grilla.
    """
    return juego[y][x][0]


def validar_posicion(pieza, juego):
    """
    Recibe una pieza y valida si esta colidiendo con alguna superficie
    """
    for posicion in pieza:
        x, y = posicion
        if not (0 <= x < ANCHO_JUEGO and 0 <= y < ALTO_JUEGO):
            return False

        posicion_ocupada = hay_superficie(juego, x, y)

        if posicion_ocupada:
            return False
    return True


def cambiar_posicion(juego, posicion):
    """
    Recibe el juego y una posicion (x,y)
    En la posicion pasada alterna entre True o False para la posicion de piezas
    """
    x, y = posicion
    juego[y][x][1] = not juego[y][x][1]


def modificar_estado_juego(posicion_actual, nueva_posicion, juego):
    """
    Recibe la posicion actual y la nueva de una pieza y el juego
    Remueve la posicion anterior y agrega a nueva al estado del juego
    """
    nuevo_estado = juego
    for posicion in zip(posicion_actual, nueva_posicion):
        cambiar_posicion(nuevo_estado, posicion[0])
        cambiar_posicion(nuevo_estado, posicion[1])
    return nuevo_estado


def mover(juego, direccion):
    """
    Mueve la pieza actual hacia la derecha o izquierda, si es posible.
    Devuelve un nuevo estado de juego con la pieza movida o el mismo estado
    recibido si el movimiento no se puede realizar.

    El parámetro direccion debe ser una de las constantes DERECHA o IZQUIERDA.
    """
    pieza = pieza_actual(juego)
    nueva_posicion = trasladar_pieza(pieza, direccion, 0)
    movimiento_valido = validar_posicion(nueva_posicion, juego)
    if not movimiento_valido:
        return juego
    return modificar_estado_juego(pieza, nueva_posicion, juego)


def tranformar_a_superficie(juego, pieza):
    """
    Recibe un juego y una pieza
    Devuelve un estado de juego donde la pieza pasa a superficie
    """
    nuevo_estado = juego
    for posicion in pieza:
        x, y = posicion
        juego[y][x][0] = not juego[y][x][0]
        juego[y][x][1] = not juego[y][x][1]
    return nuevo_estado


def buscar_lineas_completas(juego, pieza):
    """
    Recibe un juego y una pieza
    Devuelve una lista de lineas para remover
    """
    lineas = []
    for posicion in pieza:
        altura = posicion[1]
        linea_valores = [x[0] for x in juego[altura]]
        if not False in linea_valores:
            lineas.append(altura)
    return lineas


def remover_linea(juego, linea):
    """
    Recibe un juego y una linea
    Devuelve un estado de juego donde esta linea no esta mas, sin alterar la altura de juego
    """
    nuevo_estado = juego
    nuevo_estado.pop(linea)
    nuevo_estado.insert(0, [[False, False]] * ANCHO_JUEGO)
    return nuevo_estado


def remover_lineas_completas(juego, lineas):
    """
    Recibe un juego y una tupla
    Devuelve un estado de juego removiendo las lineas citadas en la tupla
    """
    nuevo_estado = juego
    for linea in lineas:
        nuevo_estado = remover_linea(nuevo_estado, linea)
    return nuevo_estado


def posicionar_nueva_pieza(juego, pieza):
    """
    Recibe un juego y una pieza
    Devulve es estado de juego con la nueva pieza posicionada
    """
    nuevo_estado = juego
    for posicion in pieza:
        cambiar_posicion(nuevo_estado, posicion)
    return nuevo_estado


def avanzar(juego, siguiente_pieza):
    """
    Avanza al siguiente estado de juego a partir del estado actual.

    Devuelve una tupla (juego_nuevo, cambiar_pieza) donde el primer valor
    es el nuevo estado del juego y el segundo valor es un booleano que indica
    si se debe cambiar la siguiente_pieza (es decir, se consolidó la pieza
    actual con la superficie).

    Avanzar el estado del juego significa:
     - Descender una posición la pieza actual.
     - Si al descender la pieza no colisiona con la superficie, simplemente
       devolver el nuevo juego con la pieza en la nueva ubicación.
     - En caso contrario, se debe
       - Consolidar la pieza actual con la superficie.
       - Eliminar las líneas que se hayan completado.
       - Cambiar la pieza actual por siguiente_pieza.

    Si se debe agregar una nueva pieza, se utilizará la pieza indicada en
    el parámetro siguiente_pieza. El valor del parámetro es una pieza obtenida
    llamando a generar_pieza().

    **NOTA:** Hay una simplificación respecto del Tetris real a tener en
    consideración en esta función: la próxima pieza a agregar debe entrar
    completamente en la grilla para poder seguir jugando, si al intentar
    incorporar la nueva pieza arriba de todo en el medio de la grilla se
    pisara la superficie, se considerará que el juego está terminado.

    Si el juego está terminado (no se pueden agregar más piezas), la funcion no hace nada,
    se debe devolver el mismo juego que se recibió.
    """
    pieza = pieza_actual(juego)
    nueva_posicion = trasladar_pieza(pieza, 0, 1)
    movimiento_valido = validar_posicion(nueva_posicion, juego)
    nuevo_estado = juego
    # pieza desende sin problem
    if movimiento_valido:  # no coliciono
        nuevo_estado = modificar_estado_juego(pieza, nueva_posicion, juego)
        return (nuevo_estado, False)
    # pieza coliciona
    if pieza[0][1] == 0:  # pieza coliciona en altura 0
        return (juego, False)
    nuevo_estado = tranformar_a_superficie(nuevo_estado, pieza)
    lineas_remover = buscar_lineas_completas(nuevo_estado, pieza)
    nuevo_estado = remover_lineas_completas(nuevo_estado, lineas_remover)
    nueva_pieza = trasladar_pieza(siguiente_pieza, ANCHO_JUEGO // 2, 0)
    nuevo_estado = posicionar_nueva_pieza(nuevo_estado, nueva_pieza)
    return (nuevo_estado, True)


def terminado(juego):
    """
    Devuelve True si el juego terminó, es decir no se pueden agregar
    nuevas piezas, o False si se puede seguir jugando.
    """
    pieza = pieza_actual(juego)
    return not validar_posicion(pieza, juego)
