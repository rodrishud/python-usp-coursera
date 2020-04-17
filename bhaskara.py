import math

a = float(input('Valor de a: '))
b = float(input('Valor de b: '))
c = float(input('Valor de c: '))

d = (b ** 2) - 4 * a * c

if d < 0:
        print('esta equação não possui raízes reais')
else:
    if d == 0:
        x = (-b + math.sqrt(d)) / (2 * a)
        print('a raiz desta equação é', x)
    else:
        x = (-b + math.sqrt(d)) / (2 * a)
        y = (-b - math.sqrt(d)) / (2 * a)
        if x < y:
            print('as raízes da equação são', x, 'e', y)
        else:
            print('as raízes da equação são', y, 'e',  x)

