def maior_elemento(lista):
    mai = lista[0]
    for c in lista:
        if mai < c:
            mai = c
    return mai