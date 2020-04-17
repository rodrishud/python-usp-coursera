def maior_primo(p):
    x = p
    cont = 0
    while True:
        for c in range(1, x + 1):
            if x % c == 0:
                cont += 1
        if cont == 2:
            print(x)
            break
        else:
            x = x - 1
            cont = 0
    return x
