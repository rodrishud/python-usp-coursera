import re


def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print()
    print()
    wal = float(input("Entre o tamanho medio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    i = 1
    textos = []
    texto = input(f'Digite o texto {i} (aperte enter para sair): ')
    print()
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f'Digite o texto {i} (aperte enter para sair): ')
        print()
    return textos


def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    return frase.split()


def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas


def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)


def compara_assinatura(as_a, as_b):
    f1 = abs(as_a[0] - as_b[0])
    f2 = abs(as_a[1] - as_b[1])
    f3 = abs(as_a[2] - as_b[2])
    f4 = abs(as_a[3] - as_b[3])
    f5 = abs(as_a[4] - as_b[4])
    f6 = abs(as_a[5] - as_b[5])
    s = (f1 + f2 + f3 + f4 + f5 + f6) / 6
    return s


def tamedio(texto):
    sentencas = separa_sentencas(texto)

    frases = []
    for i in range(len(sentencas)):
        frase_aux = separa_frases(sentencas[i])
        frases.append(frase_aux)

    palavras = []
    for linha in range(len(frases)):
        for coluna in range(len(frases[linha])):
            palavras_aux = separa_palavras(frases[linha][coluna])
            palavras.append(palavras_aux)

    mtrx = []
    for linha in range(len(palavras)):
        for coluna in range(len(palavras[linha])):
            mtrx.append(palavras[linha][coluna])
    palavras = mtrx[:]

    total_letras = 0
    total_palavras = len(palavras)
    for lin in range(len(palavras)):
        for col in range(len(palavras[lin])):
            total_letras += len(str(palavras[lin][col]))

    tam = total_letras / total_palavras
    return tam


def tyto(texto):
    p = separa_palavras(texto)
    num = n_palavras_diferentes(p)
    tt = num / len(p)
    return tt


def hale(texto):
    p = separa_palavras(texto)
    num = n_palavras_unicas(p)
    hl = num / len(p)
    return hl


def tamset(texto):
    s = separa_sentencas(texto)
    soma = 0
    x = 0
    while x < len(s):
        soma += len(s[x])
        x += 1
    tam = soma / len(s)
    return tam


def comset(texto):
    f = separa_frases(texto)
    s = separa_sentencas(texto)
    cs = len(f) / len(s)
    return cs


def tamfra(texto):
    f = separa_frases(texto)
    soma = 0
    x = 0
    while x < len(f):
        soma += len(f[x])
        x += 1
    tam = soma / len(f)
    return tam


def calcula_assinatura(texto):
    tm = tamedio(texto)
    tt = tyto(texto)
    hl = hale(texto)
    ts = tamset(texto)
    cs = comset(texto)
    tf = tamfra(texto)
    b = [tm, tt, hl, ts, cs, tf]
    return b


def avalia_textos(textos, ass_cp):
    c = 0
    menor = 0
    numtext = ''
    while c < len(textos):
        x = calcula_assinatura(textos[c])
        s = compara_assinatura(ass_cp, x)
        if menor == 0:
            menor = s
            numtext = c
        else:
            if s < menor:
                menor = s
                numtext = c
        c += 1
    return numtext + 1


modelo = le_assinatura()
print()
lista = le_textos()

print(f'O autor do texto {avalia_textos(lista, modelo)} está infectado com COH-PIAH')
