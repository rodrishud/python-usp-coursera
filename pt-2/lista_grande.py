from random import randint


def lista_grande(n):
    lista = []
    for c in range(n):
        aux = randint(0, 9999)
        lista.append(aux)
    return lista