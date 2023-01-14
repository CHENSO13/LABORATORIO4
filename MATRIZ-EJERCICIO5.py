def matriz_simetrica(matriz):
    n = len(matriz)
    simetrica = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            simetrica[i][j] = matriz[j][i]
    return simetrica

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz_simetrica(matriz))