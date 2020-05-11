def imprime_matriz(matriz):
    for l in range(len(matriz)):
        for c in range(len(matriz[l])):
            if c == len(matriz[-1]) - 1:
                print(f'{matriz[l][c]}')
            else:
                print(f'{matriz[l][c]}', end=' ')
