from random import randrange
jogos = list()
qtdjogos = int(input('Quantos jogos serão? '))
for _ in range(qtdjogos):
    jogo = [randrange(1,60),randrange(1,60),randrange(1,60),randrange(1,60),randrange(1,60),randrange(1,60)]
    jogos.append(jogo)
print('Seus jogos serão:')
for num, element in enumerate(jogos):
    print(f'Jogo {num+1}: {element}')