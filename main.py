import heapq

# Algoritmo de solución con programación dinámica


def huffman_dp(simbolos, frecuencias):
    n = len(simbolos)
    tabla = [[0] * n for _ in range(n)]

    for i in range(n):
        tabla[i][i] = frecuencias[i]

    for longitud in range(2, n+1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            tabla[i][j] = float('inf')

            for k in range(i, j):
                costo = tabla[i][k] + tabla[k + 1][j]
                if costo < tabla[i][j]:
                    tabla[i][j] = costo

            for k in range(i, j+1):
                tabla[i][j] += frecuencias[k]

    return tabla[0][n-1]

# Algoritmo de solución con enfoque greedy


class NodoHuffman:
    def __init__(self, simbolo=None, frecuencia=0, izquierda=None, derecha=None):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = izquierda
        self.derecha = derecha

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


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

# Algoritmo de programación dinámica
resultado_dp = huffman_dp(simbolos, frecuencias)
print("Costo óptimo con programación dinámica:", resultado_dp)

# Algoritmo greedy
resultado_greedy = huffman_greedy(simbolos, frecuencias)
print("Árbol de Huffman con enfoque greedy:", resultado_greedy)
