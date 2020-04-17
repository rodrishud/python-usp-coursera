from math import hypot
from math import floor

def é_hipotenusa(n):
    x = 1
    y = 1
    h = hypot(x, y)
    if n == h and h == floor(h):
        return True
    else:
        while n != h and x <= n and y <= n:
            h = hypot(x, y)
            if n == h and h == floor(h):
                return True
            else:
                x += 1
                if x == n:
                    if x == n and y == n:
                        return False
                    else:
                        x = 1
                        y += 1


def soma_hipotenusas(n):
    soma = 0
    for c in range(1, n + 1):
        x = é_hipotenusa(c)
        if x == True:
            soma += c
    return soma
