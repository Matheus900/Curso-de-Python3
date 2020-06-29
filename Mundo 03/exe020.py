jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantas partidas o jogador {jogador["nome"]} jogou? '))
print('=-='*15)
for c in range(tot):
    partidas.append(f'>>>>Quantos gols na partida {c}? ')
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}.')
