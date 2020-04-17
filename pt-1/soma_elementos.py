def soma_elementos(x):
    soma = 0
    for c in x:
        if soma == 0:
            soma = c
        else:
            soma += c
    return soma