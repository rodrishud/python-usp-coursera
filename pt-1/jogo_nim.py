def computador_escolhe_jogada(n, m):
    x = m
    while True:
        tot = n - x
        if tot % (m + 1) == 0:
            break
        else:
            x = x - 1
    if x == 0:
        x = m
        tot = n - x
    if tot > 0:
        print(f'O computador tirou {x} peça(s).'
              f'\nAgora restam {tot} peça(s) no tabuleiro.')
        print()
    else:
        print(f'O computador tirou {x} peça(s).'
              f'\nFim do jogo! O computador ganhou!')
    return x


def usuario_escolhe_jogada(n, m):
    while True:
        x = int(input('Quantas peças você vai tirar? '))
        tot = n - x
        print()
        if x > m or x <= 0:
            print('Oops! Jogada inválida! Tente de novo.')
            print()
        else:
            break

    print(f'Voce tirou {x} peça(s).'
          f'\nAgora restam {tot} peça(s).')
    print()
    return x


def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()

    if n % (m + 1) == 0:
        print('Voce começa!')
        print()
        n -= usuario_escolhe_jogada(n, m)

        while True:
            n -= computador_escolhe_jogada(n, m)
            if n == 0:
                break
            else:
                n -= usuario_escolhe_jogada(n, m)
                if n == 0:
                    break
    else:
        print('Computador começa!')
        print()
        n -= computador_escolhe_jogada(n, m)
        while True:
            n -= usuario_escolhe_jogada(n, m)
            if n == 0:
                break
            else:
                n -= computador_escolhe_jogada(n, m)
                if n == 0:
                    break


esc = ' '
while esc != 1 and esc != 2:
    esc = int(input('Bem-vindo ao jogo do NIM! Escolha:\n'
                    '\n1 - para jogar uma partida isolada\n'
                    '2 - para jogar um campeonato '))
    if esc != 1 and esc != 2:
        print('Inválido')
        print()
print()

if esc == 1:
    print('Voce escolheu uma partida isolada!')
    print()
    partida()

if esc == 2:
    cont = 0

    print('Voce escolheu um campeonato!')
    print()

    print('**** Rodada 1 ****')
    print()
    partida()
    cont += 1
    print()

    print('**** Rodada 2 ****')
    print()
    partida()
    cont += 1
    print()

    print('**** Rodada 3 ****')
    print()
    partida()
    cont += 1
    print()

    print('**** Final do campeonato! ****')
    print()
    print(f'Placar: Você 0 x {cont} Computador')
