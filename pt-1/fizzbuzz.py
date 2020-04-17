x = int(input('Insira um número: '))

if (x % 3) == 0 and (x % 5) == 0:
    print('FizzBuzz')
else:
    print('{}'.format(x))