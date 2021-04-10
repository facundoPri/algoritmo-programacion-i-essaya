import csv
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


def cargar_piezas(ruta):
    """
    Recibe la ruta del achivo con las pieza
    Devuelve una tupla de tuplas con las
    """
    piezas = {}
    with open(ruta) as piezas_archivo:
        for pieza in piezas_archivo:
            pieza_valores = pieza.split(" ")
            nombre = pieza_valores[-1].replace('\n','')
            index_descarte = pieza_valores.index("#")
            posiciones = pieza_valores[:index_descarte]
            # TODO: mejorar esto
            piezas[nombre] = tuple(
                        tuple(sorted(
                                tuple(int(x) for x in x.split(","))
                                for x in x.split(";")
                        ))
                        for x in posiciones
)
    return piezas


def cargar_teclas(ruta):
    """
    Recibe una ruta y devuelve un diccionario con la accion de la tecla
    """
    dic_teclas = {}
    with open(ruta) as teclas:
        for linea in teclas:
            linea = linea.replace(" ", "")
            linea = linea.replace("\n", "")
            if linea:
                tecla, accion = linea.split("=")
                dic_teclas[tecla] = accion
    return dic_teclas


def mostrar_tabla_records(ruta):
    """
    Recibe la ruta del archivo con la tabla de puntos
    Devuelve una matrix con los resultados
    """
    tabla_record = []
    with open(ruta) as records:
        lector = csv.DictReader(records, fieldnames=["Nombre", "Puntos"], delimiter=";")
        for puntos in lector:
            resultado = (puntos["Nombre"], int(puntos["Puntos"]))
            tabla_record.append(resultado)
    return tabla_record


def es_record(puntuaje, tabla_records):
    """
    Recibe el puntuaje y la tabla de records
    Devuelve si el puntuaje tiene que ser agredado a la tabla o no
    """
    resultado = False
    if len(tabla_records) < 10:
        resultado = True
    if tabla_records and puntuaje > tabla_records[-1][1]:
        resultado = True
    return resultado


def guardar_puntuaje(ruta, nombre, puntos):
    """
    Recibe una ruta, un nombre y un puntuaje
    Anota y ordena este puntuaje
    """
    tabla_records = mostrar_tabla_records(ruta)
    anotar = es_record(puntos, tabla_records)
    if anotar:
        tabla_records.append((nombre, puntos))
        tabla_records = sorted(tabla_records, key=lambda x: x[1], reverse=True)
    if len(tabla_records) >= 10:
        tabla_records = tabla_records[:10]
    with open(ruta, "w") as records:
        tabla = csv.writer(records, delimiter=";")
        tabla.writerows(tabla_records)


def guardar_partida(ruta, juego, puntuaje, siguiente_pieza):
    """
    Recibe una ruta de guardado y el estado del juego en el momento de guardado
    Guarda el estado del juego en el archivo de la ruta
    """
    with open(ruta, "w") as partida:
        # partida.write(f"juego = {juego}")
        # partida.write("\n")
        # partida.write(f"puntuaje = {puntuaje}")
        # partida.write("\n")
        # partida.write(f"siguiente_pieza = {siguiente_pieza}")
        csv_writer = csv.writer(partida)
        pieza = ''
        for coordenada in siguiente_pieza:
            pieza+= f"{coordenada[0]}"
            pieza+= f"{coordenada[1]}"
        for linea in juego:
            nueva_linea = []
            for valor in linea:
                nueva_linea.append(f"{valor[0]},{valor[1]}")
            csv_writer.writerow(nueva_linea)
        partida.write(f"puntuaje = {puntuaje}")
        partida.write("\n")
        partida.write(f"siguiente_pieza = {pieza}")


def cargar_partida(ruta):
    """
    Recibe la ruta del archivo donde esta la partida guardada
    """
    partida = {}
    with open(ruta) as partida_guardada:
        csv_reader = csv.reader(partida_guardada)
        juego = []
        puntuaje = 0
        siguiente_pieza = []
        for linea in csv_reader:
            if linea[0].startswith("puntuaje"):
                linea[0].replace("\n", "")
                valores = linea[0].split(" = ")
                puntuaje = float(valores[1])
            elif linea[0].startswith("siguiente_pieza"):
                linea[0].replace("\n", "")
                valores = linea[0].split(" = ")
                siguiente_pieza = []
                for index,num in enumerate(valores[1]):
                    if index%2==0:
                        siguiente_pieza.append([])
                    siguiente_pieza[-1].append(int(num))
            else:
                nueva_linea = [] 
                for valor in linea:
                   nuevo_valor = valor.split(",")
                   nueva_linea.append([nuevo_valor[0]=="True",nuevo_valor[1]=="True"])
                juego.append(nueva_linea)
        partida['juego'] = juego
        partida['puntuaje'] = puntuaje
        partida['siguiente_pieza'] = siguiente_pieza
    return partida


def generar_pieza(piezas, pieza=None):
    """
    Genera una nueva pieza de entre PIEZAS al azar. Si se especifica el parámetro pieza
    se generará una pieza del tipo indicado. Los tipos de pieza posibles
    están dados por las constantes CUBO, Z, S, I, L, L_INV, T.

    El valor retornado es una tupla donde cada elemento es una posición
    ocupada por la pieza, ubicada en (0, 0). Por ejemplo, para la pieza
    I se devolverá: ( (0, 0), (0, 1), (0, 2), (0, 3) ), indicando que
    ocupa las posiciones (x = 0, y = 0), (x = 0, y = 1), ..., etc.
    """
    pieza_opcion = ["CUBO", "Z", "S", "I", "L", "L_INV","T" ]
    if not pieza:
        pieza = pieza_opcion[randint(0, len(piezas) - 1)]
    return piezas[pieza][0]


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
        # if not (0 <= x <= ANCHO_JUEGO and 0 <= y <= ALTO_JUEGO):
        # return pieza
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
    nuevo_estado = juego.copy()
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


def buscar_rotacion(pieza_actual, piezas):
    """
    Recibe una pieza y un diccionarion con todas las piezas
    Devuelve la siguiente rotacion
    """
    nombre_pieza = [nombre for (nombre, posiciones) in piezas.items() if pieza_actual in posiciones][0]
    siguiente_pieza = None
    pieza = piezas[nombre_pieza]
    index_pieza_actual = pieza.index(pieza_actual)
    siguiente_index = (index_pieza_actual + 1) % len(pieza)
    siguiente_pieza = pieza[siguiente_index]
    return siguiente_pieza


def rotar(juego, piezas):
    """
    Recibe el estado del juego actual y las pocisiones de las piezas
    Devuelve el estado del juego con la pieza actual rotada
    """
    pieza = list(pieza_actual(juego))
    # pieza_ordenada = ordenar_por_coordenadas(pieza_a_rotar)
    pieza = sorted(pieza)
    # primer_posicion = pieza_ordenada[0]
    pos_1 = pieza[0]
    x, y = pos_1
    # pieza_en_origen = trasladar_pieza(pieza_ordenada, -primer_posicion)
    pieza_en_origen = trasladar_pieza(pieza, -x, -y)
    # siguiente_rotacion = buscar_rotacion(pieza_en_origen)
    siguiente_rotacion = buscar_rotacion(pieza_en_origen, piezas)
    # devolver trasladar_pieza(siguiente_rotacion, primer_posicion)
    pieza_rotada = trasladar_pieza(siguiente_rotacion, x, y)
    movimiento_valido = validar_posicion(pieza_rotada, juego)
    if not movimiento_valido:
        return juego
    return modificar_estado_juego(pieza, pieza_rotada, juego)


def tranformar_a_superficie(juego, pieza):
    """
    Recibe un juego y una pieza
    Devuelve un estado de juego donde la pieza pasa a superficie
    """
    nuevo_estado = juego.copy()
    for posicion in pieza:
        x, y = posicion
        nuevo_estado[y][x][0] = not nuevo_estado[y][x][0]
        nuevo_estado[y][x][1] = not nuevo_estado[y][x][1]
    return nuevo_estado


def buscar_lineas_completas(juego, pieza):
    """
    Recibe un juego y una pieza
    Devuelve una lista de lineas para remover
    """
    lineas = set()
    for posicion in pieza:
        altura = posicion[1]
        linea_valores = [x[0] for x in juego[altura]]
        if not False in linea_valores:
            lineas.add(altura)
    return list(lineas)


def remover_linea(juego, linea):
    """
    Recibe un juego y una linea
    Devuelve un estado de juego donde esta linea no esta mas, sin alterar la altura de juego
    """
    nuevo_estado = juego.copy()
    nuevo_estado.pop(linea)
    nuevo_estado.insert(0, [[False, False] for i in range(ANCHO_JUEGO)])
    return nuevo_estado


def remover_lineas_completas(juego, lineas):
    """
    Recibe un juego y una tupla
    Devuelve un estado de juego removiendo las lineas citadas en la tupla
    """
    nuevo_estado = juego.copy()
    for linea in lineas:
        nuevo_estado = remover_linea(nuevo_estado, linea)
    return nuevo_estado


def posicionar_nueva_pieza(juego, pieza):
    """
    Recibe un juego y una pieza
    Devulve es estado de juego con la nueva pieza posicionada
    """
    nuevo_estado = juego.copy()
    for posicion in pieza:
        x, y = posicion
        nuevo_estado[y][x][1] = True
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
    nuevo_estado = juego.copy()
    # pieza desende sin problem
    if movimiento_valido:  # no coliciono
        nuevo_estado = modificar_estado_juego(pieza, nueva_posicion, juego)
        return (nuevo_estado, False)
    # pieza coliciona
    if not validar_posicion(pieza, juego):  # pieza coliciona en altura 0
        return (nuevo_estado, False)
    nuevo_estado = tranformar_a_superficie(nuevo_estado, pieza)
    lineas_remover = buscar_lineas_completas(nuevo_estado, pieza)
    if lineas_remover:
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
