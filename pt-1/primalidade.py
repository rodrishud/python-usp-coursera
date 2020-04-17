n = int(input('Digite um número inteiro: '))
x = n
divisor = 1
cont = 0

while divisor <= x:
    resto = x % divisor
    if resto == 0:
        cont += 1
    divisor += 1

if cont > 2:
    print('não primo')
else:
    print('primo')
