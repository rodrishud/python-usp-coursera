l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

x = 1
while x <= a:
    n = 1
    while n <= l:
        print('#', end='')
        n += 1
        if n > l:
            print(end='\n')
    x += 1