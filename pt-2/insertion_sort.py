def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]
        j = i - 1
        while j >= 0 and valor < lista[j]:
            lista[j+1] = lista[j]
            lista[j] = valor
            j -= 1
    return lista