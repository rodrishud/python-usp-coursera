def ordena(lista):
    fim = len(lista)
    for i in range(fim - 1):
        posicaoDoMinimo = i
        for j in range(i + 1, fim):
            if lista[j] < lista[posicaoDoMinimo]:
                posicaoDoMinimo = j
        lista[i], lista[posicaoDoMinimo] = lista[posicaoDoMinimo], lista[i]
    return lista