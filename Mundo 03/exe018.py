from random import randint
from time import sleep
from operator import itemgetter
players = {'Jogador 1': randint(1,6),
            'Jogador 2': randint(1,6),
            'Jogador 3': randint(1,6),
            'Jogador 4': randint(1,6),}

for k, v in players.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1.5)

ranking = {}
ranking = sorted(players.items(), key=itemgetter(1), reverse=True)
print('=-='* 15)
print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i+1}º Lugar: {v[0]} com {v[1]}.')
    sleep(1.5)
print('>>> FIM <<<')