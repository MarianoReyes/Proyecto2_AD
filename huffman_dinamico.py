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

simbolos = ['A', 'B', 'C', 'D']
frecuencias = [10, 20, 15, 5]

resultado_dp = huffman_dp(simbolos, frecuencias)
print("Costo óptimo con programación dinámica:", resultado_dp)
