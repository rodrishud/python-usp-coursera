def primeiro_lex(lista):
    menor = ''
    for c in range(len(lista)):
        if menor == '':
            menor = lista[c]
        else:
            x = 0
            while x < len(lista[c]):
                if ord(lista[c][x]) == ord(menor[x]):
                    x += 1
                else:
                    if ord(lista[c][x]) < ord(menor[x]):
                        menor = lista[c]
                        break
                    else:
                        break
    return menor