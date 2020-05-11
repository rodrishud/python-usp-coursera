def soma_matrizes(m1, m2):
    if len(m1) == len(m2):
        linhas = len(m1)
        for c in range(linhas):
            if len(m1[c]) == len(m1[-1]) and len(m1[c]) == len(m2[c]):
                if len(m2[c]) == len(m2[-1]):
                    colunas = len(m2[-1])
                    x = True
                else:
                    return False
            else:
                return False
        if x == True:
            matriz = []
            lista = []
            aux = 0
            for l in range(linhas):
                matriz.append(lista)
                lista.clear()
                for c in range(colunas):
                    aux = (m1[l][c] + m2[l][c])
                    lista.append(aux)
            return matriz
    else:
        return False
