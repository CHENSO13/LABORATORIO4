#diagonal principal
matriz = [[5, 5, 4],
          [6, 6, 41],
          [6, 6, 77]]

long = len(matriz)
for i in range(long):
    print(matriz[i][i])

diagonalprincipal = []

long = len(matriz)
for i in range(long):
    diagonalprincipal.append(matriz[i][i])
