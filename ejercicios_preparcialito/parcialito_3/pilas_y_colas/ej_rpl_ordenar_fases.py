from cola import Cola
from pila import Pila

def ordenar_fases(fases):
    '''
    DOC: Completar
    '''
    ultimo = fases._ultimo.dato
    primer = fases.ver_frente()
    while not fases.esta_vacia():
        frente = fases.desencolar()
        ultimo_ordenado = fases._ultimo.dato if not frente == primer else 0
        if frente > ultimo_ordenado:
            print(frente)
            fases.encolar(frente)
            if frente == ultimo:
                break


fases = Cola()
fases.encolar(1)
fases.encolar(2)
fases.encolar(6)
fases.encolar(3)
fases.encolar(5)
fases.encolar(4)
fases.encolar(5)
fases.encolar(6)
fases.encolar(7)

ordenar_fases(fases)
