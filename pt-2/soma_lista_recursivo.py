def soma_lista(lista):

    if len(lista) == 1:
        return lista[0]

    elif len(lista) == 2:
        lista1 = []
        lista1.append(lista[0] + lista[1])
        return lista1[0]

    else:
        a = lista[0]
        b = lista[1]

        lista.pop(0)
        lista.pop(0)

        lista.append(a + b)
        return soma_lista(lista)
