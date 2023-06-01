import numpy as np
import heapq
import time
import matplotlib.pyplot as plt


class Nodo:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia


def Huffman_DP(pares):
    simbolos, frecuencias = zip(*pares)
    n = len(simbolos)
    tabla = np.inf * np.ones((n + 1, n + 1))

    for i in range(n):
        tabla[i][i] = frecuencias[i]

    for longitud in range(2, n + 1):
        for i in range(n - longitud + 1):
            j = i + longitud - 1
            tabla[i][j] = np.inf

            for k in range(i, j):
                costo = tabla[i][k] + tabla[k + 1][j]
                if costo < tabla[i][j]:
                    tabla[i][j] = costo

            for k in range(i, j + 1):
                tabla[i][j] += frecuencias[k]

    return tabla[0][n - 1]


def Huffman_Greedy(pares):
    simbolos, frecuencias = zip(*pares)
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


tamanos = list(
    range(1, 30)
)  # limitamos a 30 debido al costo computacional de la programación dinámica
tiempos_DP = []
tiempos_Greedy = []

for n in tamanos:
    pares = [
        (str(i), i + 1) for i in range(n)
    ]  # Aquí generamos los pares símbolo-frecuencia

    inicio = time.time()
    Huffman_DP(pares)
    fin = time.time()
    tiempos_DP.append(fin - inicio)

    inicio = time.time()
    Huffman_Greedy(pares)
    fin = time.time()
    tiempos_Greedy.append(fin - inicio)

plt.plot(tamanos, tiempos_DP, label="Programación Dinámica")
plt.plot(tamanos, tiempos_Greedy, label="Algoritmo Greedy")
plt.xlabel("Tamaño de Entrada")
plt.ylabel("Tiempo de Ejecución")
plt.legend()
plt.show()


def generar_codigos(nodo, codigo_actual="", codigos={}):
    if nodo is None:
        return

    if nodo.simbolo is not None:
        codigos[nodo.simbolo] = codigo_actual

    generar_codigos(nodo.izquierda, codigo_actual + "0", codigos)
    generar_codigos(nodo.derecha, codigo_actual + "1", codigos)

    return codigos
