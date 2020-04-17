def n_primos(x):
    y = x
    q = 0
    while y > 1:
        cont = 0
        for c in range(1, x + 1):
            if y % c == 0:
                cont += 1
        if cont == 2:
            q += 1
        y -= 1
    return q

