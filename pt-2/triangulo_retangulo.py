def main():
    t = Triangulo(1, 3, 5)
    print(t.retangulo)

    u = Triangulo(3, 4, 5)
    print(u.retangulo)


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def retangulo(self):
        maior = self.a
        if maior < self.b:
            maior = self.b
        if maior < self.c:
            maior = self.c

        x = False

        if self.a == maior:
            if maior ** 2 == (self.b ** 2) + (self.c ** 2):
                x = True
        if self.b == maior:
            if maior ** 2 == (self.a ** 2) + (self.c ** 2):
                x = True
        if self.c == maior:
            if maior ** 2 == (self.a ** 2) + (self.b ** 2):
                x = True
        return x

main()