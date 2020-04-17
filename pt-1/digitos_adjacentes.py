n = int(input('Digite um número inteiro: '))

x = n
ultimo = x % 10
x = x // 10
adj = False

while x > 0 and not adj:
    atual = x % 10
    if atual == ultimo:
        adj = True
    ultimo = atual
    x = x // 10

if adj:
    print('sim')
else:
    print('não')
