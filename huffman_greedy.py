import heapq

class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierda=None, derecha=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

    def __str__(self, nivel=0):
        indentacion = '  ' * nivel
        cadena = f'{indentacion}{self.frecuencia}\n'

        if self.simbolo is not None:
            cadena += f'{indentacion}({self.simbolo})\n'

        if self.izquierda is not None:
            cadena += f'{indentacion}Izquierda:\n'
            cadena += self.izquierda.__str__(nivel+1)

        if self.derecha is not None:
            cadena += f'{indentacion}Derecha:\n'
            cadena += self.derecha.__str__(nivel+1)

        return cadena


def huffman_greedy(simbolos, frecuencias):
    n = len(simbolos)
    cola_prioridad = []

    for i in range(n):
        nodo = NodoHuffman(simbolos[i], frecuencias[i])
        heapq.heappush(cola_prioridad, nodo)

    while len(cola_prioridad) > 1:
        nuevo_nodo = NodoHuffman()
        nodo1 = heapq.heappop(cola_prioridad)
        nodo2 = heapq.heappop(cola_prioridad)
        nuevo_nodo.izquierda = nodo1
        nuevo_nodo.derecha = nodo2
        nuevo_nodo.frecuencia = nodo1.frecuencia + nodo2.frecuencia
        heapq.heappush(cola_prioridad, nuevo_nodo)

    return cola_prioridad[0]


simbolos = ['A', 'B', 'C', 'D']
frecuencias = [10, 20, 15, 5]

resultado_greedy = huffman_greedy(simbolos, frecuencias)
print("Árbol de Huffman con enfoque greedy:\n", resultado_greedy)
