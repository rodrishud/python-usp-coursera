def main():
    t1 = Triangulo(6, 8, 10)
    t2 = Triangulo(3, 4, 5)
    print(t1.semelhantes(t2))


class Triangulo:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def semelhantes(self, triangulo):
        lista1 = [self.a, self.b, self.c]
        lista2 = [triangulo.a, triangulo.b, triangulo.c]

        lista1.sort()
        lista2.sort()

        razao = lista1[0] / lista2[0]
        if lista1[1] / lista2[1] == razao and lista1[2] / lista2[2] == razao:
            return True
        else:
            return False
