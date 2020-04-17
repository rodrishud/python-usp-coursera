n = int(input('Digite o valor de n: '))
x = 1
cont = 1

while cont < (2 * n):
    if x % 2 != 0:
        print(x)
    x += 1
    cont += 1
