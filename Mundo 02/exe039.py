from random import choice
cont = 0
while True:
    print('=-=' * 20)
    num = int(input('Diga um valor: '))
    op = input('Par ou Ímpar:[P/I] ').upper().strip()
    print('=-=' * 20)
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    pc = choice(lista)
    res = num + pc
    if op == 'P':
        if res % 2 == 0:
            print(f'Você jogou {num} e o computador jogou {pc}. Total de {res} DEU PAR\n\nVOCE GANHOU\n')
            cont += 1
        else:
            print(f'Você jogou {num} e o computador jogou {pc}. Total de {res} DEU ÍMPAR\n\n')
            print('VOCE PERDEU')
            print('=-=' * 20)
            print('GAME OVER')
            print('=-=' * 20)
            print(f'Você ganhou {cont} vezes')
            break
    if op == 'I':
        if res % 2 == 0:
            print(f'Você jogou {num} e o computador jogou {pc}. Total de {res} DEU PAR\n\n')
            print('VOCE PERDEU')
            print('=-=' * 20)
            print('GAME OVER')
            print('=-=' * 20)
            print(f'Você ganhou {cont} vezes')
            break
        else:
            print(f'Você jogou {num} e o computador jogou {pc}. Total de {res} DEU ÍMPAR\n\nVOCE GANHOU\n')
            cont += 1