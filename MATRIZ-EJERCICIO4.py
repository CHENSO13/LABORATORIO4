
#transpuesta de una matriz


def transpuesta():
    matriz = [[5, 6, 8],
              [4, 7, 3],
              [2, 8, 1]]

    transpuesta = []
    for i in range(len(matriz[0])):
        fila = []
        for j in range(len(matriz)):
            fila.append(matriz[j][i])
        transpuesta.append(fila)

    for fila in transpuesta:
        for elemento in fila:
            print(elemento, end=' ')
        print()
transpuesta()

# if resultado == None:
#     print("No se puede sumar")
# else:
#     for fila in resultado:
#         print("[", end=" ")
#         for elemento in fila:
#             print(elemento,end=" ")
#         print("]")
