def remove_repetidos(lista):
    x = []
    for c in lista:
        if c not in x:
            x.append(c)
    x.sort()
    return x