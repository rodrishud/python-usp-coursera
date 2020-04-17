n = int(input('Digite um número inteiro: '))

x = n
total = 0
digito = 0

while x > 0:
    digito = x % 10
    x = x // 10
    total = total + digito
print(total)