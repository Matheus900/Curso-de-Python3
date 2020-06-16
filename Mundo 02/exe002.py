from random import choice
print('O pc vai escolher um número entre 1 e 5. Tente adivinhar qual será.')
numero = int(input('Escolha seu número: '))
possibilidade = [1, 2, 3, 4, 5]
pc = choice(possibilidade)
if numero == pc:
    print('Você acertou.\nPARABÉNS!')
else:
    print('Você fracassou.')