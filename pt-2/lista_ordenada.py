def ordenada(lista):
    fim = len(lista)
    for c in range(fim - 1):
        pos = c
        for j in range(c + 1, fim):
            if lista[j] > lista[pos]:
                pos = j
            else:
                return False
    return True