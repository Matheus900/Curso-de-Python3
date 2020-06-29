def main():
    jogador = str(input('Nome do jogador: '))
    qtdgols = str(input('Número de gols: '))
    print(ficha(jogador, qtdgols))


def ficha(nome, gols):
    if len(nome) == 0:
        nome = '<desconhecido>'
    if len(gols) == 0:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato'


main()
