l = int(input('digite a largura: '))
a = int(input('digite a altura: '))

x = 1
while x <= a:
    if x == 1 or x == a:
        print('#' * l)
    else:
        print('#' + ' ' * (l - 2) + '#')
    x += 1