def conta_letras(frase, contar="vogais"):
    cont = 0
    if contar == "vogais":
        for c in range(len(frase)):
            if frase[c] in "AaÁáEeÉéIiÍíOoÓóUuÚú":
                cont += 1

    if contar == "consoantes":
        for c in range(len(frase)):
            if frase[c] in "BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvWwXxYyZz":
                cont += 1

    return cont