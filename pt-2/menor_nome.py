def menor_nome(nomes):
    menor = 0
    nome = ''
    aux = ''
    for c in range(0, len(nomes)):
        aux = nomes[c].split()
        n = len(aux[0])

        if menor == 0:
            menor = n
            nome = aux[0]
        else:
            if menor > n:
                menor = n
                nome = aux[0]

    nome = nome.lower().capitalize()
    return nome

