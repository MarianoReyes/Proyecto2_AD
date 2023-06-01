import heapq


class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def Huffman_Greedy(simbolos, frecuencias):
    n = len(simbolos)
    colaPrioridad = []

    for i in range(n):
        nodo = Nodo(simbolos[i], frecuencias[i])
        heapq.heappush(colaPrioridad, nodo)

    while len(colaPrioridad) > 1:
        nodo1 = heapq.heappop(colaPrioridad)
        nodo2 = heapq.heappop(colaPrioridad)
        nuevoNodo = Nodo(None, nodo1.frecuencia + nodo2.frecuencia)
        nuevoNodo.izquierda = nodo1
        nuevoNodo.derecha = nodo2
        heapq.heappush(colaPrioridad, nuevoNodo)

    return colaPrioridad[0]


def generar_codigos(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return

    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = codigo_actual

    generar_codigos(nodo.izquierda, codigo_actual + "0", codigos)
    generar_codigos(nodo.derecha, codigo_actual + "1", codigos)

    return codigos


simbolos = ["a", "b", "c", "d", "e", "f"]
frecuencias = [5, 9, 12, 13, 16, 45]

nodo_raiz = Huffman_Greedy(simbolos, frecuencias)
codigos = generar_codigos(nodo_raiz)
print(codigos)
