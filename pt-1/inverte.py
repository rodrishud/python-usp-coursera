lista = []

while True:
    x = int(input('Digite um número: '))
    if x == 0:
        break
    else:
        lista.append(x)

tam = len(lista) - 1
while tam >= 0:
    print(lista[tam])
    tam -= 1
