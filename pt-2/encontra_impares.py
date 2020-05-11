def encontra_impares(lista):
    listaVazia = []
    if len(lista) == 1:
        if lista[0] == 1 or lista[0] % 2 == 1:
            return lista
        else:
            return listaVazia

    else:
        cont = 0

        for c in range(len(lista)):
            if lista[c] % 2 == 1:
                cont += 1

        if cont == len(lista):
            return lista

        else:
            listaAux = []
            if lista[0] % 2 == 1:
                listaAux.append(lista[0])
                lista.pop(0)
                lista.extend(listaAux)
            else:
                lista.pop(0)
            return encontra_impares(lista)
