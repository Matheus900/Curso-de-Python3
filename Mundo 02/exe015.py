from random import choice
from time import sleepprint('Vamos jogar jokenpô?')
user = int(input("""1 - Pedra\n 
2 - Papel\n 
3 - Tesoura\n 
Opção: """))
lista_pc = [1, 2, 3]
escolha_pc = choice(lista_pc)
print('JO', end=''), sleep(0.5)
print('KEN', end=''), sleep(0.5)
print('PO!!!'), sleep(0.5)
if user == 1:
    if escolha_pc == 1:
        print('O pc jogou Pedra'), sleep(0.5)
        print('Empate')
    elif escolha_pc == 2:
        print('O pc jogou Papel'), sleep(0.5)
        print('Derrota')
    else:
        print('O pc jogou Tesoura'), sleep(0.5)
        print('Vitória')
elif user == 2:
    if escolha_pc == 1:
        print('O pc jogou Pedra'), sleep(0.5)
        print('Vitória')
    elif escolha_pc == 2:
        print('O pc jogou Papel'), sleep(0.5)
        print('Empate')
    else:
        print('O pc jogou Tesoura'), sleep(0.5)
        print('Derrota')
elif user == 3:
    if escolha_pc == 1:
        print('O pc jogou Pedra'), sleep(0.5)
        print('Derrota')
    elif escolha_pc == 2:
        print('O pc jogou Papel'), sleep(0.5)
        print('Vitória')
    else:
        print('O pc jogou Tesoura'), sleep(0.5)
        print('Empate')
else:
    print('[ERROR]\nOpção inválida')